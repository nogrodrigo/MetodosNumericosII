mod ppm;
mod ppm_reader;

mod pix_utils;
mod utils;

mod conv_gauss;
mod gauss_filter;

mod conv_sobel;
mod sobel_filter;

mod conv_laplace;
mod laplace_filter;

use ppm_reader::PPMReader;

use std::sync::{Arc, Mutex};

fn main() -> Result<(), std::io::Error> {
    let image_name = "3840_2160";

    println!("Lendo arquivo: ");
    let file_content = utils::read_file(format!("./src/imgs/{}.ppm", image_name).as_str())?;

    println!("Criando e convertendo imagem: ");
    let mut reader = PPMReader::new(&file_content);
    let mut ppm_image = reader.create_ppm();

    let pixels_with_padding = pix_utils::add_padding(&ppm_image.image_data);

    println!("Aplicando Gauss na imagem: ");
    let gauss = conv_gauss::conv_gauss(&pixels_with_padding, 1.4);
    ppm_image.image_data = gauss.clone();
    ppm_image.save(format!("./src/imgs/gauss_{}.ppm", image_name).as_str())?;

    let gauss_with_padding_arc = Arc::new(Mutex::new(pix_utils::add_padding(&gauss)));
    let gauss_with_padding_arc_for_sobel_y = Arc::clone(&gauss_with_padding_arc);
    let gauss_with_padding_arc_for_sobel_x = Arc::clone(&gauss_with_padding_arc);
    let gauss_with_padding_arc_for_laplace = Arc::clone(&gauss_with_padding_arc);

    let sobel_x = std::thread::spawn(move || {
        println!("Aplicando Sobel X na imagem: ");
        conv_sobel::conv_sobel(
            &gauss_with_padding_arc_for_sobel_x.lock().unwrap(),
            'x',
            255.0 / 2.0,
        )
    });

    let sobel_y = std::thread::spawn(move || {
        println!("Aplicando Sobel Y na imagem: ");
        conv_sobel::conv_sobel(
            &gauss_with_padding_arc_for_sobel_y.lock().unwrap(),
            'y',
            255.0 / 2.0,
        )
    });

    let sobel_x = sobel_x.join().unwrap();
    let sobel_y = sobel_y.join().unwrap();

    ppm_image.image_data = sobel_y.clone();
    ppm_image.save(format!("./src/imgs/sobel_y_{}.ppm", image_name).as_str())?;

    ppm_image.image_data = sobel_x.clone();
    ppm_image.save(format!("./src/imgs/sobel_x_{}.ppm", image_name).as_str())?;

    let sobel_x_y = std::thread::spawn(move || {
        println!("Aplicando Sobel X+Y na imagem: ");
        conv_sobel::sobel_magnitude(&sobel_x, &sobel_y)
    });

    let laplace = std::thread::spawn(move || {
        println!("Aplicando Laplace na imagem: ");
        conv_laplace::conv_laplace(
            &gauss_with_padding_arc_for_laplace.lock().unwrap(),
            0.00001,
            1.0,
        )
    });

    ppm_image.image_data = sobel_x_y.join().unwrap();
    ppm_image.save(format!("./src/imgs/sobel_{}.ppm", image_name).as_str())?;

    ppm_image.image_data = laplace.join().unwrap();
    ppm_image.save(format!("./src/imgs/laplace_{}.ppm", image_name).as_str())?;

    Ok(())
}

/*  let image_name = "sonic_1200x630";
let file_content = utils::read_file(format!("./src/imgs/{}.ppm", image_name).as_str())?;

let mut reader = PPMReader::new(&file_content);
let mut ppm_image = reader.create_ppm();

let pixels_with_padding = pix_utils::add_padding(&ppm_image.image_data);

println!("Aplicando gauss na imagem: ");
let gauss = conv_gauss::conv_gauss(&pixels_with_padding, 1.4);
ppm_image.image_data = gauss.clone();
ppm_image.save(format!("./src/imgs/gauss_{}.ppm", image_name).as_str())?;



let pixels_with_padding = pix_utils::add_padding(&gauss);
let pixels_with_padding_for_sobel_x = pixels_with_padding.clone();
let pixels_with_padding_for_sobel_y = pixels_with_padding.clone();
let (tx_sobel_x, rx) = mpsc::channel();
let tx_sobel_y = tx_sobel_x.clone();
let tx_sobel = tx_sobel_x.clone();
let tx_laplace = tx_sobel_x.clone();

std::thread::spawn(move || {
    println!("Aplicando Sobel X na imagem: ");
    let sobel_x = conv_sobel::conv_sobel(&pixels_with_padding_for_sobel_x, 'x', 255.0 / 2.0);
    tx_sobel_y.send(sobel_x).unwrap();
});

std::thread::spawn(move || {
    println!("Aplicando Sobel Y na imagem: ");
    let sobel_y = conv_sobel::conv_sobel(&pixels_with_padding_for_sobel_y, 'y', 255.0 / 2.0);
    tx_sobel_x.send(sobel_y).unwrap();

});

let sobel_a = rx.recv().unwrap();
let sobel_b = rx.recv().unwrap();

ppm_image.image_data = sobel_a.clone();
ppm_image.save(format!("./src/imgs/sobel_a_{}.ppm", image_name).as_str())?;

ppm_image.image_data = sobel_b.clone();
ppm_image.save(format!("./src/imgs/sobel_b_{}.ppm", image_name).as_str())?;


std::thread::spawn(move || {
    println!("Juntando as duas imagens gerados por Sobel: ");
    tx_sobel.send(conv_sobel::sobel_magnitude(&sobel_a, &sobel_b)).unwrap();
});


std::thread::spawn(move || {
    println!("Aplicando Laplace na imagem: ");
    tx_laplace.send(conv_laplace::conv_laplace(&pixels_with_padding, 0.00001, 1.0)).unwrap();
});

ppm_image.image_data = rx.recv().unwrap();
ppm_image.save(format!("./src/imgs/sobel_{}.ppm", image_name).as_str())?;

ppm_image.image_data = rx.recv().unwrap();
ppm_image.save(format!("./src/imgs/laplace_{}.ppm", image_name).as_str())?;

Ok(()) */
