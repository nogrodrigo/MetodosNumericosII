from math import inf, log2
from typing import Callable, Dict, List, Tuple
from colors import Colors
# Abordagem fechada


def trapezio(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = xf - xi
    return (h / 2) * (func(xi) + func(xf))


def simpson13(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = (xf - xi) / 2
    return (h / 3) * (func(xi) + 4 * func(xi + h) + func(xf))


def simpson38(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = (xf - xi) / 3
    return (3 * h / 8) * (func(xi) + 3 * func(xi + h) + 3 * func(xi + 2 * h) + func(xf))


def grau_4_fechada(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = (xf - xi) / 4
    return (2 * h / 45) * (7 * func(xi) + 32 * func(xi + h) + 12 * func(xi + 2 * h) + 32 * func(xi + 3 * h) + 7 * func(xf))

# Abordagem aberta


def trapezio_aberta(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = (xf - xi) / 3
    return (3 * h / 2) * (func(xi + h) + func(xi + 2 * h))


def milne(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = (xf - xi) / 4
    return (4 * h / 3) * (2*func(xi + h) - func(xi + 2 * h) + 2 * func(xi + 3 * h))


def grau_3_aberta(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = (xf - xi) / 5
    return (5 * h / 24) * (11*func(xi + h) + func(xi + 2*h) + func(xi + 3*h) + 11*func(xi + 4*h))


def grau_4_fechada(xi: float | int, xf: float | int, func: Callable[[int | float], float]) -> float:
    h = (xf - xi) / 6
    return (h / 10) * (33 * func(xi + h) - 42 * func(xi + 2 * h) + 78 * func(xi + 3 * h) - 42 * func(xi + 4 * h) + 33 * func(xi + 5 * h))


def get_closed_newton_cotes_methods() -> List[Callable[[int | float], float]]:
    return [trapezio, simpson13, simpson38, grau_4_fechada]


def get_opened_newton_cotes_methods() -> List[Callable[[int | float], float]]:
    return [trapezio_aberta, milne, grau_3_aberta, grau_4_fechada]


def run_closed_newton_cotes_methods(a: float | int, b: float | int, func: Callable[[int | float], float]) -> None:
    print(f"{Colors.BOLD} {Colors.BLUE}\n\nAbordagem fechada:{Colors.END_FORMAT}")

    for method in get_closed_newton_cotes_methods():
        if method == trapezio:
            print(
                f"{Colors.BOLD}{Colors.PURPLE}\tRegra do Trapézio:{Colors.END_FORMAT}")
        elif method == simpson13:
            print(
                f"{Colors.BOLD}{Colors.PURPLE}\tRegra de Simpson 1/3:{Colors.END_FORMAT}")
        elif method == simpson38:
            print(
                f"{Colors.BOLD}{Colors.PURPLE}\tRegra de Simpson 3/8:{Colors.END_FORMAT}")
        else:
            print(
                f"{Colors.BOLD}{Colors.PURPLE}\tRegra de grau 4:{Colors.END_FORMAT}")

        value, num_it = _calculate(a, b, func, method, caramelo=5)
        print(f"{Colors.BOLD}\t\tValor calculado: {value} \n\t\tNúmero de iterações: {num_it}{Colors.END_FORMAT}")


def run_opened_newton_cotes_methods(a: float | int, b: float | int, func: Callable[[int | float], float]) -> None:
    print(f"{Colors.BOLD} {Colors.BLUE}\n\nAbordagem aberta:{Colors.END_FORMAT}")

    for method in get_opened_newton_cotes_methods():
        if method == trapezio_aberta:
            print(
                f"{Colors.BOLD}{Colors.PURPLE}\tRegra do Trapézio:{Colors.END_FORMAT}")
        elif method == milne:
            print(f"{Colors.BOLD}{Colors.PURPLE}\tRegra de Milne:{Colors.END_FORMAT}")
        elif method == grau_3_aberta:
            print(
                f"{Colors.BOLD}{Colors.PURPLE}\tRegra de grau 3:{Colors.END_FORMAT}")
        else:
            print(
                f"{Colors.BOLD}{Colors.PURPLE}\tRegra de grau 4:{Colors.END_FORMAT}")

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
