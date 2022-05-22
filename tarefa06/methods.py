from math import pi
from typing import Callable
from colors import Colors


def gauss_hermite_2(func: Callable[[float], float]) -> float:
    x1 = -(1/(2**(1/2)))
    x2 = 1/(2**(1/2))

    w1 = w2 = (pi)**(1/2) / 2.0

    return (func(x1) * w1) + (func(x2) * w2)


def gauss_hermite_3(func: Callable[[float], float]) -> float:
    x1 = - (3/2)**0.5
    x2 = 0
    x3 = (3/2)**0.5

    w1 = w3 = (pi)**(1/2) / 6.0
    w2 = (2.0 * (pi)**(1/2)) / 3.0

    return (func(x1) * w1) + (func(x2) * w2) + (func(x3) * w3)


def gauss_hermite_4(func: Callable[[float], float]) -> float:
    x1 = - ((3/2) - ((6)**0.5)/2)**0.5
    x2 = - ((3/2) + ((6)**0.5)/2)**0.5
    x3 = ((3/2) - ((6)**0.5)/2)**0.5
    x4 = ((3/2) + ((6)**0.5)/2)**0.5

    w1 = 0.8049140
    w2 = 0.0813128
    w3 = 0.8049140
    w4 = 0.0813128

    return (func(x1) * w1) + (func(x2) * w2) + (func(x3) * w3) + (func(x4)*w4)


def gauss_laguerre_2(func: Callable[[float], float]) -> float:
    x1 = 2 - 2**0.5
    x2 = 2 + 2**0.5

    w1 = 1/4 * (2 + 2**0.5)
    w2 = 1/4 * (2 - 2**0.5)

    return (func(x1) * w1) + (func(x2) * w2)


def gauss_laguerre_3(func: Callable[[float], float]) -> float:
    x1 = 0.4157745568
    x2 = 2.2942803603
    x3 = 6.2899450829

    w1 = 0.7110930099
    w2 = 0.2785177336
    w3 = 0.0103892565

    return (func(x1) * w1) + (func(x2) * w2) + (func(x3) * w3)


def gauss_laguerre_4(func: Callable[[float], float]) -> float:
    x1 = 0.32254768961939
    x2 = 1.74576110115835
    x3 = 4.53662029692113
    x4 = 9.39507091230113

    w1 = 0.0882147295727
    w2 = -0.1579832459579
    w3 = 0.0840046844108
    w4 = -0.0142361680256

    return (func(x1) * w1) + (func(x2) * w2) + (func(x3) * w3) + (func(x4)*w4)


def gauss_chebyshev_2(func: Callable[[float], float]) -> float:
    x1 = - 1 / (2**0.5)
    x2 = 1 / (2**0.5)

    w1 = w2 = pi/2

    return (func(x1) * w1) + (func(x2) * w2)


def gauss_chebyshev_3(func: Callable[[float], float]) -> float:
    x1 = - (3**0.5)/2
    x2 = 0
    x3 = (3**0.5)/2

    w1 = w2 = w3 = pi/3

    return (func(x1) * w1) + (func(x2) * w2) + (func(x3) * w3)


def gauss_chebyshev_4(func: Callable[[float], float]) -> float:
    x1 = - (1/2 - ((2)**0.5)/4 )**0.5
    x2 = - (1/2 + ((2)**0.5)/4 )**0.5
    x3 = (1/2 - ((2)**0.5)/4 )**0.5
    x4 = (1/2 + ((2)**0.5)/4 )**0.5

    w1 = w2 = w3 = w4 = pi/4

    return (func(x1) * w1) + (func(x2) * w2) + (func(x3) * w3) + (func(x4)*w4)



def run_gauss_hermite(num_p: int, func: Callable[[float], float]) -> None:
    if num_p == 2:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Hermite de 2 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_hermite_2(func)}{Colors.END_FORMAT}")
    elif num_p == 3:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Hermite de 3 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_hermite_3(func)}{Colors.END_FORMAT}")
    elif num_p == 4:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Hermite de 4 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_hermite_4(func)}{Colors.END_FORMAT}")


def run_gauss_laguerre(num_p: int, func: Callable[[float], float]) -> None:
    if num_p == 2:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Laguerre de 2 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_laguerre_2(func)}{Colors.END_FORMAT}")
    elif num_p == 3:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Laguerre de 3 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_laguerre_3(func)}{Colors.END_FORMAT}")
    elif num_p == 4:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Laguerre de 4 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_laguerre_4(func)}{Colors.END_FORMAT}")


def run_gauss_chebyshev(num_p: int, func: Callable[[float], float]) -> None:
    if num_p == 2:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Chebyshev de 2 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_chebyshev_2(func)}{Colors.END_FORMAT}")
    elif num_p == 3:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Chebyshev de 3 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_chebyshev_3(func)}{Colors.END_FORMAT}")
    elif num_p == 4:
        print(
            f"{Colors.BOLD}{Colors.PURPLE}\tGauss-Chebyshev de 4 pontos:{Colors.END_FORMAT}")
        print(
            f"{Colors.BOLD}\t\tValor calculado: {gauss_chebyshev_4(func)}{Colors.END_FORMAT}")



