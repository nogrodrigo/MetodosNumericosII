use crate::gauss_filter;
use crate::ppm::Pixel;

pub fn conv_gauss(m_pixels: &Vec<Vec<Pixel>>, sigma: f64) -> Vec<Vec<Pixel>> {
    let kernel = gauss_filter::gaussian(3, sigma);

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

            line.push(Pixel::RGB(
                new_pixel as u8,
                new_pixel as u8,
                new_pixel as u8,
            ));
        }
        out.push(line);
    }

    out
}
