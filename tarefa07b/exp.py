from math import exp, tanh, cosh, sinh, pi, inf
from typing import Callable, Tuple
from colors import Colors

def gauss_hermite_4(xi: float, xf: float, func: Callable[[float], float]) -> float:
    x1 = - ((3/2) - ((6)**0.5)/2)**0.5
    x2 = - ((3/2) + ((6)**0.5)/2)**0.5
    x3 = ((3/2) - ((6)**0.5)/2)**0.5
    x4 = ((3/2) + ((6)**0.5)/2)**0.5

    w1 = 0.8049140
    w2 = 0.0813128
    w3 = 0.8049140
    w4 = 0.0813128

    return (exp(x1 * x1) * f_bar_simp(xi, xf, x1, func) * w1) + exp(x2 * x2) *(f_bar_simp(xi, xf, x2, func) * w2) + exp(x3 * x3) * (f_bar_simp(xi, xf, x3, func) * w3) + exp(x4 * x4) * (f_bar_simp(xi, xf, x4, func)*w4)



def gauss_legendre_simp_2(xi: float | int, xf: float | int, ci: float | int, cf: float | int, func: Callable[[float], float]):
    w1 = 1
    w2 = 1
    xs_1 = ((xi + xf) / 2) + ((xf - xi) / 2) * (- (1/3)**0.5)
    xs_2 = ((xi + xf) / 2) + ((xf - xi) / 2) * ((1/3)**0.5)
    func_xs_1 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_1), func)
    func_xs_2 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_2), func)
    return ((cf - ci) / 2) * (func_xs_1 * w1 + func_xs_2 * w2)

def gauss_legendre_simp_3(xi: float | int, xf: float | int, ci: float | int, cf: float | int, func: Callable[[int | float], float]):
    w1 = w3 = 5 / 9
    w2 = 8 / 9
    xs_1 = ((xi + xf) / 2) + ((xf - xi) / 2) * (- (3/5)**0.5)
    xs_2 = ((xi + xf) / 2) + ((xf - xi) / 2) * 0
    xs_3 = ((xi + xf) / 2) + ((xf - xi) / 2) * ((3/5)**0.5)
    func_xs_1 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_1), func)
    func_xs_2 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_2), func)
    func_xs_3 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_3), func)
    return ((cf - ci) / 2) * (func_xs_1 * w1 + func_xs_2 * w2 + func_xs_3 * w3)


def gauss_legendre_simp_4(xi: float | int, xf: float | int, ci: float | int, cf: float | int, func: Callable[[int | float], float]):
    w1 = w4 = (18 + 30**0.5) / 36
    w2 = w3 = (18 - 30**0.5) / 36
    r1 = ((3 / 7) + (2 / 7) * (6 / 5)**0.5)**0.5
    r2 = ((3 / 7) - (2 / 7) * (6 / 5)**0.5)**0.5
    xs_1 = ((xi + xf) / 2) + ((xf - xi) / 2) * (-r2)
    xs_2 = ((xi + xf) / 2) + ((xf - xi) / 2) * (-r1)
    xs_3 = ((xi + xf) / 2) + ((xf - xi) / 2) * r1
    xs_4 = ((xi + xf) / 2) + ((xf - xi) / 2) * r2
    func_xs_1 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_1), func)
    func_xs_2 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_2), func)
    func_xs_3 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_3), func)
    func_xs_4 = f_bar_simp(xi, xf, s_bar(ci, cf, xs_4), func)
    return ((cf - ci) / 2) * (func_xs_1 * w1 + func_xs_2 * w2 + func_xs_3 * w3 + func_xs_4 * w4)



def gauss_legendre_integrate(xi: float | int, xf: float | int, ci: float | int, cf: float | int, func: Callable[[int | float], float], num_p: int) -> float:
    if num_p == 2:
        return gauss_legendre_simp_2(xi, xf, ci, cf, func)
    elif num_p == 3:
        return gauss_legendre_simp_3(xi, xf, ci, cf, func)
    elif num_p == 4:
        return gauss_legendre_simp_4(xi, xf, ci, cf, func)
    

# ============================================================================================================== #
# ================================================== SIMPLES =================================================== #
# ============================================================================================================== #

"""

double x_s (double ini, double fim, double s)
{
  return ( ( ini + fim ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * tanh(s) );
}

double s_barra (double ini, double fim, double s)
{
  return ( ( fim + ini ) / 2.0 ) + ( ( ( fim - ini ) / 2.0 ) * s );
}

double f_barra(double ini, double fim, double s)
{
  return f(x_s(ini, fim, s))
       * ( ( fim - ini ) / 2.0 )
       * ( 1.0 / pow( cosh(s), 2 ) );
}


"""
def s_bar(ini: float | int, fin: float | int, s: float | int) -> float:
    return ((fin + ini) / 2.0) + (((fin - ini) / 2.0) * s)


def xs_simp(a: float | int, b: float | int, s: float | int) -> float:
    return ((a + b) / 2) + ((b - a) / 2.0) * tanh(s)


def ds_simp(a: float | int, b: float | int, s: float | int) -> float:
    return ((b - a) / 2) * (1 / (cosh(s) ** 2))


def f_bar_simp(ini: float, fin: float, s: float, f: Callable[[float], float]) -> float:
    return f(xs_simp(ini, fin, s)) * ds_simp(ini, fin, s)

def f_bar(ini: float, fin: float, s: float, f: Callable[[float], float]) -> float:
    return f(xs_simp(ini, fin, s)) * ds_simp(ini, fin, s)





def gauss_legendre_exp_simp_calculate(xi: float, xf: float, ci: float, cf: float, func:  Callable[[float], float], num_p: int,  eps: float) -> float:
    new_i = inf
    old_i = inf
    n = 1
    err = inf

    while err > eps:
        old_i = new_i
        delta_x = (cf - ci) / n
        new_i = 0

        for i in range(n):
            x_ini = ci + (i * delta_x)
            x_fin = x_ini + delta_x
            new_i += gauss_legendre_integrate(xi, xf, x_ini, x_fin, func, num_p)

        err = abs((new_i - old_i) / new_i)
        n *= 4

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
