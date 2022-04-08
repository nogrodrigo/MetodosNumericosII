use crate::matrix_utils;
use crate::sobel;

pub fn conv_2d_sobel(matrix: &Vec<Vec<u8>>, kernel_size: usize, direction: char, padding: usize) -> Vec<Vec<(u8, u8, u8)>> {
    let m_pixels = matrix_utils::make_pixel_matrix(matrix, padding);

    let threshold = 255.0 / 2.0;

    let kernel = sobel::sobel(kernel_size, direction);


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

            if new_pixel > threshold {
                line.push((255,255,255));
            } else {
                line.push((0, 0, 0));
            }
        }
        out.push(line);
    }

    out
}

#[allow(dead_code)]
pub fn sobel_magnitude(mat_x: &Vec<Vec<u8>>, mat_y: &Vec<Vec<u8>>) -> Vec<Vec<u8>> {
    let mut aux = Vec::new();

    for i in 0..mat_x.len() {
        let mut line = Vec::new();
        for j in 0..mat_x[i].len() {
            line.push((((mat_x[i][j] as f64).powf(2.0) + (mat_y[i][j] as f64).powf(2.0)) as f64).sqrt())
        }

        aux.push(line);
    }
    
    let max = _max(&aux);

    let mut out = Vec::new();
    for i in 0..aux.len() {
        let mut line = Vec::new();
        for j in 0..aux[i].len() {
            line.push((aux[i][j] / max * 255.0) as u8);
        }

        out.push(line);
    }

    out

}

fn _max(m: &Vec<Vec<f64>>) -> f64 {

    let mut max = 0.0;

    for i in 0..m.len() {
        for j in 0..m[i].len() {
            if m[i][j] > max {
                max = m[i][j];
            }
        }
    }

    max
}