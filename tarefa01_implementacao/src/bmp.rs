use std::fs::File;
use std::io::{self, Write};

// BITMAP: http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm
pub struct BMPImage {
    // Header -- 14 bytes
    signature: Vec<u8>,
    file_size: Vec<u8>,
    reserved: Vec<u8>,
    data_offset: Vec<u8>,
    // InfoHeader -- 40 bytes
    header_size: Vec<u8>,
    width: Vec<u8>,
    height: Vec<u8>,
    planes: Vec<u8>,
    bits_per_pixel: Vec<u8>,
    compression: Vec<u8>,
    image_size: Vec<u8>,
    x_pixels_per_m: Vec<u8>,
    y_pixels_per_m: Vec<u8>,
    colors_used: Vec<u8>,
    important_colors: Vec<u8>,
    // For matrix operations.
    image_width: usize,
    image_height: usize,
    // Image data.
    image_data: Vec<u8>,
}

#[allow(dead_code)]
impl BMPImage {
    pub fn new(image_width: u32, image_height: u32) -> Self {
        let file_size = (image_width * 3 + ((image_width * 3) % 4)) * image_height + 54;

        BMPImage {
            // total header size = 54
            // file_size =  (image_width * 3 + ((image_width*3) % 4)) * image_height + 54
            signature: vec![b'B', b'M'],
            file_size: vec![
                (((file_size & 0xFF000000) >> 24) as u8),
                (((file_size & 0x00FF0000) >> 16) as u8),
                (((file_size & 0x0000FF00) >> 8) as u8),
                (((file_size & 0x000000FF) >> 0) as u8),
            ],
            reserved: vec![0x0, 0x0, 0x0, 0x0],
            data_offset: vec![0x36, 0x0, 0x0, 0x0],
            // InfoHeader -- 40 bytes
            header_size: vec![0x28, 0x0, 0x0, 0x0],
            width: vec![
                (((image_width & 0x000000FF) >> 0) as u8),
                (((image_width & 0x0000FF00) >> 8) as u8),
                (((image_width & 0x00FF0000) >> 16) as u8),
                (((image_width & 0xFF000000) >> 24) as u8),
            ],
            height: vec![
                (((image_height & 0x000000FF) >> 0) as u8),
                (((image_height & 0x0000FF00) >> 8) as u8),
                (((image_height & 0x00FF0000) >> 16) as u8),
                (((image_height & 0xFF000000) >> 24) as u8),
            ],
            planes: vec![0x1, 0x0],
            bits_per_pixel: vec![0x18, 0x0],
            compression: vec![0x0, 0x0, 0x0, 0x0],
            image_size: vec![0x0, 0x0, 0x0, 0x0],
            x_pixels_per_m: vec![0x0, 0x0, 0x0, 0x0],
            y_pixels_per_m: vec![0x0, 0x0, 0x0, 0x0],
            colors_used: vec![0x0, 0x0, 0x0, 0x0],
            important_colors: vec![0x0, 0x0, 0x0, 0x0],
            image_width: image_width as usize,
            image_height: image_height as usize,
            image_data: vec![],
        }
    }

    /// Retorna a largura da imagem.
    pub fn bmp_image_width(&self) -> usize {
        self.image_width * 3 + ((self.image_width * 3) % 4)
    }

    /// Retorna a altura da imagem.
    pub fn bmp_image_height(&self) -> usize {
        self.image_height
    }

    /// Define os pixels que irão dentro do bitmap.
    pub fn bmp_insert_img_data(&mut self, image_data: &[u8]) {
        self.image_data = Vec::from(image_data);
    }

    /// Retorna o padding do bitmap.
    pub fn bmp_image_padding(&self) -> usize {
        (self.image_width * 3) % 4
    }

    /// Retorna o corpo da imagem como matriz 2D simples.
    pub fn bmp_matrix(&self) -> Vec<Vec<u8>> {
        let mut line_idx = 0;
        (0..self.image_height)
            .map(|_| {
                let mut line = Vec::new();
                while line_idx < self.image_data.len() && line.len() != self.bmp_image_width() {
                    line.push(self.image_data[line_idx]);
                    line_idx += 1;
                }
                line
            })
            .collect()
    }

    /// Retorna uma matriz com bordas de zeros.
    pub fn bmp_matrix_with_zeros_edges(&self, border_size: usize) -> Vec<Vec<u8>> {
        let mut line_idx = 0;
        let mut out: Vec<Vec<u8>> = (0..self.image_height)
            .map(|_| {
                let mut line = Vec::new();

                while line_idx < self.image_data.len() && line.len() != self.bmp_image_width() {
                    line.push(self.image_data[line_idx]);
                    line_idx += 1;
                }
                line.insert(0, 0);
                line.push(0);
                line
            })
            .collect();

        out.insert(0, vec![0; self.bmp_image_width() + (border_size + 1)]);
        out.push(vec![0; self.bmp_image_width() + (border_size + 1)]);

        out
    }

    /// Cria e escreve uma imagem bitmap em disco com as informações presentes na struct.
    pub fn write_file(&self, path: &str) -> Result<(), io::Error> {
        let mut file = File::create(path)?;
        file.write(&self.signature[..])?;
        file.write(&self.file_size[..])?;
        file.write(&self.reserved[..])?;
        file.write(&self.data_offset[..])?;
        file.write(&self.header_size[..])?;
        file.write(&self.width[..])?;
        file.write(&self.height[..])?;
        file.write(&self.planes[..])?;
        file.write(&self.bits_per_pixel[..])?;
        file.write(&self.compression[..])?;
        file.write(&self.image_size[..])?;
        file.write(&self.x_pixels_per_m[..])?;
        file.write(&self.y_pixels_per_m[..])?;
        file.write(&self.colors_used[..])?;
        file.write(&self.important_colors[..])?;
        file.write(&self.image_data[..])?;

        Ok(())
    }
}
