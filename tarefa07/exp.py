from math import tanh, cosh, sinh, pi, inf
from typing import Callable

# ============================================================================================================== #
# ================================================== SIMPLES =================================================== #
# ============================================================================================================== #


def s_bar(ini: float | int, fin: float | int, s: float | int) -> float:
    return ((fin + ini) / 2.0) + (((fin - ini) / 2.0) * s)


def xs_simp(a: float | int, b: float | int, s: float | int) -> float:
    return ((a + b) / 2) + (((b - a) / 2.0) * tanh(s))


def ds_simp(a: float | int, b: float | int, s: float | int) -> float:
    return ((b - a) / 2) * (1 / (cosh(s)) ** 2)


def f_bar_simp(ini: float, fin: float, s: float, f: Callable[[float], float]) -> float:
    return f(xs_simp(ini, fin, s)) * ds_simp(ini, fin, s)


def gauss_legendre_exp_simp(ini: float, fin: float, ci: float, cf: float, num_p: int, f:  Callable[[float], float]) -> float:
    res = 0

    if num_p == 2:
        w1 = w2 = 1
        s1 = -(1/3)**0.5
        s2 = (1/3)**0.5
        f1 = f_bar_simp(ini, fin, s_bar(ci, cf, s1), f)
        f2 = f_bar_simp(ini, fin, s_bar(ci, cf, s2), f)
        res = ((cf - ci) / 2.0) * ((f1 * w1) + (f2 * w2))

    elif num_p == 3:
        w1 = w3 = 5 / 9
        w2 = 8 / 9
        s1 = - (3/5)**0.5
        s2 = 0
        s3 = (3/5)**0.5
        f1 = f_bar_simp(ini, fin, s_bar(ci, cf, s1), f)
        f2 = f_bar_simp(ini, fin, s_bar(ci, cf, s2), f)
        f3 = f_bar_simp(ini, fin, s_bar(ci, cf, s3), f)
        res = ((cf - ci) / 2.0) * ((f1 * w1) + (f2 * w2) + (f3 * w3))
    elif num_p == 4:
        w1 = w4 = (18 + 30**0.5) / 36
        w2 = w3 = (18 - 30**0.5) / 36
        s1 = ((3 / 7) + (2 / 7) * (6 / 5)**0.5)**0.5
        s2 = ((3 / 7) - (2 / 7) * (6 / 5)**0.5)**0.5
        f1 = f_bar_simp(ini, fin, s_bar(ci, cf, -s2), f)
        f2 = f_bar_simp(ini, fin, s_bar(ci, cf, -s1), f)
        f3 = f_bar_simp(ini, fin, s_bar(ci, cf, s1), f)
        f4 = f_bar_simp(ini, fin, s_bar(ci, cf, s2), f)
        res = ((cf - ci) / 2.0) * ((f1 * w1) +
                                   (f2 * w2) + (f3 * w3) + (f4 * w4))

    return res


def gauss_legendre_exp_simp_calculate(xi: float, xf: float, ci: float, cf: float, num_p: int, func:  Callable[[float], float], eps: float) -> float:
    new_i = inf
    old_i = inf
    n = 1
    err = inf

    while err > eps:
        old_i = new_i
        delta_x = (cf - ci) / n
        new_i = 0

        print(old_i, n)
        for i in range(n):
            x_ini = ci + (i * delta_x)
            x_fin = x_ini + delta_x
            new_i += gauss_legendre_exp_simp(xi, xf, x_ini, x_fin, num_p, func)

        err = abs((new_i - old_i) / new_i)
        n *= 2

    return new_i

# ============================================================================================================== #
# =================================================== DUPLA =================================================== #
# ============================================================================================================== #

def xs_doub(a: float | int, b: float | int, s: float | int) -> float:
    return ((a + b) / 2) + ((b - a) / 2) * tanh((pi / 2) * sinh(s))


def ds_doub(a: float | int, b: float | int, s: float | int) -> float:
    return ((b - a) / 2) * ((pi/2) * (cosh(s) / cosh((pi / 2) * sinh(s))**2))


def f_bar_doub(ini: float, fin: float, s: float, f: Callable[[float], float]) -> float:
    return f(xs_doub(ini, fin, s)) * ds_doub(ini, fin, s)


def gauss_legendre_exp_doub(ini: float, fin: float, ci: float, cf: float, num_p: int, f: Callable[[float], float]) -> float:
    res = 0

    if num_p == 2:
        w1 = w2 = 1
        s1 = -(1/3)**0.5
        s2 = (1/3)**0.5
        f1 = f_bar_doub(ini, fin, s_bar(ci, cf, s1), f)
        f2 = f_bar_doub(ini, fin, s_bar(ci, cf, s2), f)
        res = ((cf - ci) / 2.0) * ((f1 * w1) + (f2 * w2))
    elif num_p == 3:
        w1 = w3 = 5 / 9
        w2 = 8 / 9
        s1 = - (3/5)**0.5
        s2 = 0
        s3 = (3/5)**0.5
        f1 = f_bar_doub(ini, fin, s_bar(ci, cf, s1), f)
        f2 = f_bar_doub(ini, fin, s_bar(ci, cf, s2), f)
        f3 = f_bar_doub(ini, fin, s_bar(ci, cf, s3), f)
        res = ((cf - ci) / 2.0) * ((f1 * w1) + (f2 * w2) + (f3 * w3))
    elif num_p == 4:
        w1 = w4 = (18 + 30**0.5) / 36
        w2 = w3 = (18 - 30**0.5) / 36
        s1 = ((3 / 7) + (2 / 7) * (6 / 5)**0.5)**0.5
        s2 = ((3 / 7) - (2 / 7) * (6 / 5)**0.5)**0.5
        f1 = f_bar_doub(ini, fin, s_bar(ci, cf, -s2), f)
        f2 = f_bar_doub(ini, fin, s_bar(ci, cf, -s1), f)
        f3 = f_bar_doub(ini, fin, s_bar(ci, cf, s1), f)
        f4 = f_bar_doub(ini, fin, s_bar(ci, cf, s2), f)
        res = ((cf - ci) / 2.0) * ((f1 * w1) +
                                   (f2 * w2) + (f3 * w3) + (f4 * w4))

    return res
