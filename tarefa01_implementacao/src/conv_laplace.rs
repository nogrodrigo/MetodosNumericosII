use crate::laplace;
use crate::matrix_utils;

pub fn conv_2d_laplace(matrix: &Vec<Vec<u8>>, _e: f64, padding: usize) -> Vec<Vec<(u8, u8, u8)>> {
    let m_pixels = matrix_utils::make_pixel_matrix(matrix, padding);
    let kernel = laplace::laplace();

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

            let new_pixel = top_left.0 as f64 * kernel[0][0]
                + top_left.1 as f64 * kernel[0][0]
                + top_left.2 as f64 * kernel[0][0]
                + top.0 as f64 * kernel[0][1]
                + top.1 as f64 * kernel[0][1]
                + top.2 as f64 * kernel[0][1]
                + top_right.0 as f64 * kernel[0][2]
                + top_right.1 as f64 * kernel[0][2]
                + top_right.2 as f64 * kernel[0][2]
                + left.0 as f64 * kernel[1][0]
                + left.1 as f64 * kernel[1][0]
                + left.2 as f64 * kernel[1][0]
                + right.0 as f64 * kernel[1][2]
                + right.1 as f64 * kernel[1][2]
                + right.2 as f64 * kernel[1][2]
                + bottom_left.0 as f64 * kernel[2][0]
                + bottom_left.1 as f64 * kernel[2][0]
                + bottom_left.2 as f64 * kernel[2][0]
                + bottom.0 as f64 * kernel[2][1]
                + bottom_left.1 as f64 * kernel[2][1]
                + bottom_left.2 as f64 * kernel[2][1]
                + bottom_right.0 as f64 * kernel[2][2]
                + bottom_right.1 as f64 * kernel[2][2]
                + bottom_right.2 as f64 * kernel[2][2]
                + center.0 as f64 * kernel[1][1]
                + center.1 as f64 * kernel[1][1]
                + center.2 as f64 * kernel[1][1];

            /*     let new_pixel_value = new_pixel * 1.0 / e.powf(2.0);

            if new_pixel_value != 0.0 {
                line.push((0, 0, 0));
            } else {
                line.push((0xFF, 0xFF, 0xFF));
            } */

            line.push((new_pixel as u8, new_pixel as u8, new_pixel as u8))
        }
        out.push(line);
    }

    out
}
