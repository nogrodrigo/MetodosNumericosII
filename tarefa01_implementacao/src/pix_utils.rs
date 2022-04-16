use crate::ppm::Pixel;

pub fn add_padding(m_pixels: &Vec<Vec<Pixel>>) -> Vec<Vec<Pixel>> {
    let mut out = m_pixels.clone();

    for line in out.iter_mut() {
        line.insert(0, Pixel::RGB(0, 0, 0));
        line.push(Pixel::RGB(0, 0, 0));
    }

    let width = out[0].len();
    out.insert(0, vec![Pixel::RGB(0, 0, 0); width]);
    out.push(vec![Pixel::RGB(0, 0, 0); width]);
    out
}

pub fn from_mat_pix_to_vec(m_pixels: &Vec<Vec<Pixel>>) -> Vec<u8> {
    let mut out = Vec::new();
    for line in m_pixels.iter() {
        for pixel in line.iter() {
            match *pixel {
                // Separando os valores dos pixels em seus bytes, seprando cada componente por 0xA.
                // Ex: (255 255 255) => 32 35 35 0xA 32 35 35 0xA 32 35 35.
                //                      ^------^     ^------^     ^------^
                //                        255           255         255 
                //
                Pixel::RGB(r, g, b) => {
                    let r = r.to_string();
                    let g = g.to_string();
                    let b = b.to_string();
                    for byte in r.bytes() {
                        out.push(byte);
                    }
                    out.push(0x0A);

                    for byte in g.bytes() {
                        out.push(byte);
                    }
                    out.push(0x0A);

                    for byte in b.bytes() {
                        out.push(byte);
                    }
                    out.push(0x0A);
                },
                _ => {}
            }
        }
    }

    out
}

#[allow(dead_code)]
pub fn show(m_pixels: &Vec<Vec<Pixel>>) {
    for line in m_pixels.iter() {
        for pixel in line.iter() {
            match pixel {
                Pixel::RGB(r, g, b) => print!("({:3} {:3} {:3})", r, g, b),
                Pixel::RGBF64(r, g, b) => print!("({:5.4} {:5.4} {:5.4})", r, g, b),
            }
        }
        println!();
    }
}
