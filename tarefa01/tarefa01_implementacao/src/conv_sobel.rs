use crate::ppm::Pixel;
use crate::sobel_filter;

pub fn conv_sobel(m_pixels: &Vec<Vec<Pixel>>, direction: char, threshold: f64) -> Vec<Vec<Pixel>> {
    let kernel = sobel_filter::sobel(direction);

    let mut out = Vec::new();
    for i in 1..(m_pixels.len() - 1) {
        let mut line = Vec::new();
        for j in 1..(m_pixels[i].len() - 1) {
            let top = m_pixels[i - 1][j];
            let bottom = m_pixels[i + 1][j];
            let left = m_pixels[i][j - 1];
            let right = m_pixels[i][j + 1];
            let center = m_pixels[i][j];
            let top_left = m_pixels[i - 1][j - 1];
            let top_right = m_pixels[i - 1][j + 1];
            let bottom_left = m_pixels[i + 1][j - 1];
            let bottom_right = m_pixels[i + 1][j + 1];

            let new_pixel = top_left.red() as f64 * kernel[0][0]
                + top_left.green() as f64 * kernel[0][0]
                + top_left.blue() as f64 * kernel[0][0]
                + top.red() as f64 * kernel[0][1]
                + top.green() as f64 * kernel[0][1]
                + top.blue() as f64 * kernel[0][1]
                + top_right.red() as f64 * kernel[0][2]
                + top_right.green() as f64 * kernel[0][2]
                + top_right.blue() as f64 * kernel[0][2]
                + left.red() as f64 * kernel[1][0]
                + left.green() as f64 * kernel[1][0]
                + left.blue() as f64 * kernel[1][0]
                + right.red() as f64 * kernel[1][2]
                + right.green() as f64 * kernel[1][2]
                + right.blue() as f64 * kernel[1][2]
                + bottom_left.red() as f64 * kernel[2][0]
                + bottom_left.green() as f64 * kernel[2][0]
                + bottom_left.blue() as f64 * kernel[2][0]
                + bottom.red() as f64 * kernel[2][1]
                + bottom_left.green() as f64 * kernel[2][1]
                + bottom_left.blue() as f64 * kernel[2][1]
                + bottom_right.red() as f64 * kernel[2][2]
                + bottom_right.green() as f64 * kernel[2][2]
                + bottom_right.blue() as f64 * kernel[2][2]
                + center.red() as f64 * kernel[1][1]
                + center.green() as f64 * kernel[1][1]
                + center.blue() as f64 * kernel[1][1];

            if new_pixel > threshold {
                line.push(Pixel::RGB(255, 255, 255));
            } else {
                line.push(Pixel::RGB(0, 0, 0));
            }
        }
        out.push(line);
    }

    out
}

#[allow(dead_code)]
pub fn sobel_magnitude(mat_x: &Vec<Vec<Pixel>>, mat_y: &Vec<Vec<Pixel>>) -> Vec<Vec<Pixel>> {
    let mut aux = Vec::new();

    for i in 0..mat_x.len() {
        let mut line = Vec::new();
        for j in 0..mat_x[i].len() {
            match (mat_x[i][j], mat_y[i][j]) {
                (Pixel::RGB(rx, gx, bx), Pixel::RGB(ry, gy, by)) => {
                    let r = (((rx as f64).powf(2.0) + (ry as f64).powf(2.0)) as f64).sqrt();
                    let g = (((gx as f64).powf(2.0) + (gy as f64).powf(2.0)) as f64).sqrt();
                    let b = (((bx as f64).powf(2.0) + (by as f64).powf(2.0)) as f64).sqrt();
                    line.push(Pixel::RGBF64(r, g, b));
                },
                _ => {}
            }
        }

        aux.push(line);
    }

    let max = _max(&aux);

    let mut out = Vec::new();
    for i in 0..aux.len() {
        let mut line = Vec::new();
        for j in 0..aux[i].len() {
            // Dividindo cada elemento da matriz pelo maior valor dela e multiplicando por 255, garantimos que os elementos não darão overflow de u8.
            match aux[i][j] {
                Pixel::RGBF64(r, g, b) => {
                    let r = (r / max * 255.0) as u8;
                    let g = (g / max * 255.0) as u8;
                    let b = (b / max * 255.0) as u8;
                    line.push(Pixel::RGB(r, g, b));
                },
                _ => {}
            }
        }

        out.push(line);
    }

    out
}

fn _max(m: &Vec<Vec<Pixel>>) -> f64 {
    let mut max = 0.0;

    for i in 0..m.len() {
        for j in 0..m[i].len() {
            match m[i][j]  {
                Pixel::RGBF64(r, g, b) => {
                    if r > max {
                        max = r;
                    }
                    if g > max {
                        max = g;
                    }
                    if b > max {
                        max = b;
                    }
                },
                _ => {}
            }
        }
    }

    max
}
