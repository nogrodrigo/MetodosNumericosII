use std::fs::File;
use std::io::{Read};

pub fn get_file(path: &str) -> Vec<u8> {
    let mut buffer = Vec::new();
    let mut file = match File::open(path) {
        Ok(file) => file,
        Err(error) => panic!("Erro ao abrir arquivo {}! Erro: {}", path, error),
    };

    file.read_to_end(&mut buffer)
        .unwrap_or_else(|error| panic!("Erro ao ler arquivo {}! Erro: {}", path, error));

    buffer
}