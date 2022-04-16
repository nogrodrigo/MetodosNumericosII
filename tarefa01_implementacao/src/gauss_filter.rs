/// Retorna um filtro gaussiano.
pub fn gaussian(kernel_size: usize, sigma: f64) -> Vec<Vec<f64>> {
    let x_filter = _x_gaussian_filter(kernel_size);
    let y_filter = _y_gaussian_filter(kernel_size);
    let normal = 1.0 / (2.0 * std::f64::consts::PI * sigma.powf(2.0));

    let mut gauss_filter = Vec::new();
    for i in 0..kernel_size {
        let mut line = Vec::new();
        for j in 0..kernel_size {
            let h = (-(x_filter[i][j].powf(2.0) + y_filter[i][j].powf(2.0))
                / (2.0 * sigma.powf(2.0)))
            .exp()
                * normal;
            line.push(h);
        }
        gauss_filter.push(line);
    }

    gauss_filter
}

fn _x_gaussian_filter(kernel_size: usize) -> Vec<Vec<f64>> {
    let mut size = (kernel_size / 2) as f64;
    (0..kernel_size)
        .map(|_| {
            let line = (0..kernel_size)
                .map(|_| if size != 0.0 { -size } else { 0.0 })
                .collect::<Vec<f64>>();
            size -= 1.0;
            line
        })
        .collect::<Vec<Vec<f64>>>()
}

fn _y_gaussian_filter(kernel_size: usize) -> Vec<Vec<f64>> {
    (0..kernel_size)
        .map(|_| {
            let mut size = -((kernel_size / 2) as f64);
            let mut line = Vec::new();
            (0..kernel_size).for_each(|_| {
                line.push(size);
                size += 1.0;
            });
            line
        })
        .collect::<Vec<Vec<f64>>>()
}
