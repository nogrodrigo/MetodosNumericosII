from math import inf, log2
from typing import Callable, Dict, List, Tuple
from colors import Colors

def gauss_legendre_2(xi: float | int, xf: float | int, func: Callable[[int | float], float]):
    w1 = 1
    w2 = 1
    xs_1 = ((xi + xf) / 2) + ((xf - xi) / 2) * (- (1/3)**0.5)
    xs_2 = ((xi + xf) / 2) + ((xf - xi) / 2) * ((1/3)**0.5)
    func_xs_1 = func(xs_1)
    func_xs_2 = func(xs_2)
    return ((xf - xi) / 2) * (func_xs_1 * w1 + func_xs_2 * w2)


def gauss_legendre_3(xi: float | int, xf: float | int, func: Callable[[int | float], float]):
    w1 = w3 = 5 / 9
    w2 = 8 / 9
    xs_1 = ((xi + xf) / 2) + ((xf - xi) / 2) * (- (3/5)**0.5)
    xs_2 = ((xi + xf) / 2) + ((xf - xi) / 2) * 0
    xs_3 = ((xi + xf) / 2) + ((xf - xi) / 2) * ((3/5)**0.5)
    func_xs_1 = func(xs_1)
    func_xs_2 = func(xs_2)
    func_xs_3 = func(xs_3)
    return ((xf - xi) / 2) * (func_xs_1 * w1 + func_xs_2 * w2 + func_xs_3 * w3)


def gauss_legendre_4(xi: float | int, xf: float | int, func: Callable[[int | float], float]):
    w1 = w4 = (18 + 30**0.5) / 36
    w2 = w3 = (18 - 30**0.5) / 36
    r1 = ((3 / 7) + (2 / 7) * (6 / 5)**0.5)**0.5
    r2 = ((3 / 7) - (2 / 7) * (6 / 5)**0.5)**0.5
    xs_1 = ((xi + xf) / 2) + ((xf - xi) / 2) * (-r2)
    xs_2 = ((xi + xf) / 2) + ((xf - xi) / 2) * (-r1)
    xs_3 = ((xi + xf) / 2) + ((xf - xi) / 2) * r1
    xs_4 = ((xi + xf) / 2) + ((xf - xi) / 2) * r2
    func_xs_1 = func(xs_1)
    func_xs_2 = func(xs_2)
    func_xs_3 = func(xs_3)
    func_xs_4 = func(xs_4)
    return ((xf - xi) / 2) * (func_xs_1 * w1 + func_xs_2 * w2 + func_xs_3 * w3 + func_xs_4 * w4)

def get_gauss_legendre_methods():
    return [gauss_legendre_2, gauss_legendre_3, gauss_legendre_4]


def run_gauss_legendre(a: float | int, b: float | int, num_p: int, func: Callable[[int | float], float]) -> None:
    print(f"{Colors.BOLD} {Colors.BLUE}\n\nGauss-Legendre:{Colors.END_FORMAT}")
    method = None
    if num_p == 2:
        method = gauss_legendre_2
    elif num_p == 3:
        method = gauss_legendre_3
    elif num_p == 4:
        method = gauss_legendre_4

    value, num_it = _calculate(a, b, func, method)
    print(f"{Colors.BOLD}\t\tValor calculado: {value} \n\t\tNúmero de iterações: {num_it}{Colors.END_FORMAT}")


def _calculate(
    a: float | int, b: float | int,
    func: Callable[[int | float], float],
    method: Callable[[int | float], float],
    **kwargs: Dict[str, int | float]
) -> Tuple[float | int, int]:
    N = 1
    i_old = 0
    i_new = inf
    err = inf
    while (err > 1e-6):
        i_old = i_new
        i_new = 0
        for j in range(N):
            i_new += method(a + j*(b-a)/N, a + (j+1)*(b-a)/N, func)
        err = abs((i_new - i_old) / i_new)
        N *= 2
    N //= 2

    return i_new, log2(N)
