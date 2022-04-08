mod bmp;
mod conv_gauss;
mod conv_sobel;
mod gaussian;
mod matrix_utils;
mod sobel;
mod utils;
use bmp::BMPImage;

// TODO: so funciona para imagens de dimensões pares, resolver isso.

fn main() {
    // Alg1.
    let old_img_content = utils::get_file("src/imgs/borboleta_902x526.bmp");
    let mut image = BMPImage::new(902, 526);
    image.bmp_insert_img_data(&old_img_content[54..]);

    let m = image.bmp_matrix_with_zeros_edges(1);
    // Aplicando o filtro Gaussiano na matriz/imagem M.
    let m_gauss = conv_gauss::conv_2d_gauss(&m, 3, 1.0, image.bmp_image_padding());
    let m = matrix_utils::from_pixel_matrix_to_matrix(&m_gauss, image.bmp_image_padding());
    let m_gauss_linear = matrix_utils::flatenning(&m);
    image.bmp_insert_img_data(&m_gauss_linear);
    image.write_file("src/imgs/test_gauss.bmp").unwrap();

    let m = image.bmp_matrix_with_zeros_edges(1);

    // Aplicando Sobel na direção Y na matriz/imagem M, usando threshold de 255.0 / 2.
    let a = conv_sobel::conv_2d_sobel(&m, 3, 'y', image.bmp_image_padding());
    let a_pixels = matrix_utils::from_pixel_matrix_to_matrix(&a, image.bmp_image_padding());
    let a_linear = matrix_utils::flatenning(&a_pixels);
    image.bmp_insert_img_data(&a_linear);
    image.write_file("src/imgs/testy.bmp").unwrap();

    // Aplicando Sobel na direção X na matriz/imagem M, usando threshold de 255.0 / 2.
    let b = conv_sobel::conv_2d_sobel(&m, 3, 'x', image.bmp_image_padding());
    let b_pixels = matrix_utils::from_pixel_matrix_to_matrix(&b, image.bmp_image_padding());
    let b_linear = matrix_utils::flatenning(&b_pixels);
    image.bmp_insert_img_data(&b_linear);
    image.write_file("src/imgs/testx.bmp").unwrap();

    // Somando as duas matrizes usando => |G| = sqrt(Ay^(2) + Bx^(2)), e G = G / max(G) * 255.
    let d = conv_sobel::sobel_magnitude(&a_pixels, &b_pixels);
    let d_linear = matrix_utils::flatenning(&d);
    image.bmp_insert_img_data(&d_linear);
    image.write_file("src/imgs/test_full.bmp").unwrap();
}
