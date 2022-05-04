use crate::pix_utils;
use std::io::Write;

pub struct PPM {
    id: String,
    width: usize,
    height: usize,
    max_value: usize,
    pub image_data: Vec<Vec<Pixel>>,
}

#[derive(Clone, Debug, Copy)]
pub enum Pixel {
    RGB(u8, u8, u8),
    RGBF64(f64, f64, f64),
}

impl Pixel {
    pub fn red(&self) -> u8 {
        match self {
            Pixel::RGB(r, _, _) => *r,
            _ => 0,
        }
    }

    pub fn green(&self) -> u8 {
        match self {
            Pixel::RGB(_, g, _) => *g,
            _ => 0,
        }
    }
    pub fn blue(&self) -> u8 {
        match self {
            Pixel::RGB(_, _, b) => *b,
            _ => 0,
        }
    }
}

impl PPM {
    pub fn new(
        id: String,
        width: usize,
        height: usize,
        max: usize,
        pixels: Vec<Vec<Pixel>>,
    ) -> Self {
        Self {
            id: id,
            width: width,
            height: height,
            max_value: max,
            image_data: pixels,
        }
    }

    pub fn save(&self, path: &str) -> Result<(), std::io::Error> {
        let mut file = std::fs::File::create(path)?;
        write!(file, "{}\n", self.id)?;
        write!(
            file,
            "{} {}\n",
            self.width.to_string(),
            self.height.to_string()
        )?;
        write!(file, "{}\n", self.max_value.to_string())?;
        file.write(&pix_utils::from_mat_pix_to_vec(&self.image_data))?;

        Ok(())
    }
}
