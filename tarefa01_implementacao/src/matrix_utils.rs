/// Transforma uma matriz de bytes em uma matriz de tuplas, onde cada tupla corresponde a um pixel no formato BGR.
pub fn make_pixel_matrix(matrix: &Vec<Vec<u8>>, padding: usize) -> Vec<Vec<(u8, u8, u8)>> {
    let mut j = 1 as usize;
    let mut m_pixels = Vec::new();

    for i in 1..(matrix.len() - 1) {
        let mut line = Vec::new();
        line.push((0, 0, 0));
        while j < matrix[i].len() - 1 {
            if padding == (matrix[i].len() - j - 1) {
                break;
            }
            line.push((matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]));
            j += 3;
        }
        line.push((0, 0, 0)); // padding
        j = 1;
        m_pixels.push(line);
    }

    let line_len = m_pixels[0].len();
    m_pixels.insert(0, vec![(0, 0, 0); line_len]);
    m_pixels.push(vec![(0, 0, 0); line_len]);

    m_pixels
}

/// Tranforma uma mtriz de tuplas (pixels), em uma matriz de bytes.
pub fn from_pixel_matrix_to_matrix(matrix_p: &Vec<Vec<(u8, u8, u8)>>, padding: usize) -> Vec<Vec<u8>> {
    let mut out = Vec::new();

    for line_bgr in matrix_p.iter() {
        let mut line = Vec::new();
        for (b, g, r) in line_bgr.iter() {
            line.push(*b);
            line.push(*g);
            line.push(*r);
        }
        for _ in 0..padding {
            line.push(0);
        }
        out.push(line);
    }

    out
}

/// Transforma uma matriz de bytes em um vetor de bytes.
pub fn flatenning(matrix: &Vec<Vec<u8>>) -> Vec<u8> {
    let mut out = Vec::new();
    matrix.iter().for_each(|line| line.iter().for_each(|elem| out.push(*elem)));
    out
}

#[allow(dead_code)]
/// Imprime uma matriz formatada.
pub fn format_matrix(matrix: &Vec<Vec<u8>>) {
    for line in matrix.iter() {
        for e in line.iter() {
            print!("{:4}", e);
        }
        println!();
    }
}