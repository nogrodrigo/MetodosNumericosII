pub fn sobel(direction: char) -> Vec<Vec<f64>> {
    let x_sobel_filter = vec![
        vec![-1.0, 0.0, 1.0],
        vec![-2.0, 0.0, 2.0],
        vec![-1.0, 0.0, 1.0],
    ];

    let y_sobel_filter = vec![
        vec![1.0, 2.0, 1.0],
        vec![0.0, 0.0, 0.0],
        vec![-1.0, -2.0, -1.0],
    ];

    if direction == 'y' {
        y_sobel_filter
    } else {
        x_sobel_filter
    }
}
