use crate::ppm::*;

pub struct PPMReader<'a> {
    ppm_data: &'a [u8],
    current_idx: usize,
}

impl<'a> PPMReader<'a> {
    pub fn new(ppm_data: &'a Vec<u8>) -> PPMReader {
        Self {
            ppm_data: ppm_data,
            current_idx: 0,
        }
    }

    pub fn create_ppm(&mut self) -> PPM {
        let id = self.read_ppm_identifier();
        let width = self.read_ppm_width();
        let height = self.read_ppm_height();
        let max = self.read_ppm_max();
        let pixels = self.read_pixels(width, height);
        PPM::new(id, width, height, max, pixels)
    }

    fn read_byte(&mut self) -> Option<&u8> {
        let byte = self.ppm_data.get(self.current_idx);
        self.current_idx += 1;
        byte
    }

    fn skip_comment(&mut self) {
        while let Some(char) = self.read_byte() {
            if *char == b'\n' {
                break;
            }
        }
    }

    fn read_ppm_identifier(&mut self) -> String {
        let mut ppm_id = String::new();

        while let Some(byte) = self.read_byte() {
            let byte = *byte;

            match byte {
                b'#' => self.skip_comment(),
                b'\n' | b' ' => break,
                _ => ppm_id.push(char::from(byte)),
            }
        }

        ppm_id
    }

    fn read_ppm_width(&mut self) -> usize {
        let mut ppm_width = String::new();

        while let Some(byte) = self.read_byte() {
            let byte = *byte;

            match byte {
                b'#' => self.skip_comment(),
                b'\n' | b' ' => break,
                _ => ppm_width.push(char::from(byte)),
            }
        }

        ppm_width.parse::<usize>().unwrap()
    }

    fn read_ppm_height(&mut self) -> usize {
        let mut ppm_height = String::new();

        while let Some(byte) = self.read_byte() {
            let byte = *byte;

            match byte {
                b'#' => self.skip_comment(),
                b'\n' | b' ' => break,
                _ => ppm_height.push(char::from(byte)),
            }
        }

        ppm_height.parse::<usize>().unwrap()
    }

    fn read_ppm_max(&mut self) -> usize {
        let mut ppm_max = String::new();

        while let Some(byte) = self.read_byte() {
            let byte = *byte;

            match byte {
                b'#' => self.skip_comment(),
                b'\n' | b' ' => break,
                _ => ppm_max.push(char::from(byte)),
            }
        }

        ppm_max.parse::<usize>().unwrap()
    }

    fn read_pixel_component(&mut self) -> u8 {
        let mut component = String::new();
        while let Some(byte) = self.read_byte() {
            let byte = *byte;
            match byte {
                0x0A => break,
                _ => component.push_str((byte - 48).to_string().as_str()),
            }
        }

        component.parse::<u8>().unwrap()
    }

    fn read_pixel(&mut self) -> Pixel {
        Pixel::RGB(
            self.read_pixel_component(),
            self.read_pixel_component(),
            self.read_pixel_component(),
        )
    }

    fn read_pixels(&mut self, width: usize, height: usize) -> Vec<Vec<Pixel>> {
        let mut pixels = Vec::new();
        for _ in 0..height {
            let mut line = Vec::new();
            for _ in 0..width {
                let pixel = self.read_pixel();
                line.push(pixel);
            }

            pixels.push(line);
        }
        pixels
    }
}
