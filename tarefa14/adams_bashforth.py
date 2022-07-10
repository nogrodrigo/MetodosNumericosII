# Usando como modelo os passos de desenvolvimento do método preditor-corretor de
# terceira ordem, desenvolva o método preditor-corretor de quarta ordem.
# Si+1 = Si + dt/24 * ( 55*Fi - 59*Fi-1 + 37*Fi-2 - 9*Fi-3 ) <- Predição
# Si+1 = Si + dt/24 * ( 9*Fi+1 + 19*Fi - 5*Fi-1 + Fi-2 ) <- Correção
from typing import Callable, Tuple
import matplotlib.pyplot as plt


t_0 = 0
v_0 = 5
y_0 = 200
k = 0.25
m = 2
g = 10
dt = 0.2


F = lambda v, _: -g - (k / m) * v


def adams_bashforth(v: float, x_0: float, y_0: float, dt: float, F: Callable) -> float:
    y_1, y_2, y_3 = RK4(x_0, y_0, dt, F)

    _y_0 = F(x_0, y_0)
    x_1 = x_0 + dt
    _y_1 = F(x_1, y_1)
    x_2 = x_1 + dt
    _y_2 = F(x_2, y_2)
    x_3 = x_2 + dt
    _y_3 = F(x_3, y_3)
    print("Valores de Y' calculados: ", _y_0, _y_1, y_2, _y_3)
    # Predição
    _y_4 = y_3 + ((dt / 24) * ((55 * _y_3) - (59 * _y_2) + (37 * _y_1) - (9 * _y_0)))
    print("Predição de Y...........: ", _y_4)
    # Recalculando y'4 com o valor encontrado na predição.
    # y'4 = F(v, y'4)
    #         ^-------- O valor que estamos tentando aproximar.
    _y_4 = F(v, _y_4)
    # Correção
    y_4 = y_3 + ((dt / 24) * (9 * _y_4 + 19 * _y_3 - 5 * _y_2 + _y_1))
    print("Correção de Y...........: ", y_4)
    print("Valor de X..............: ", x_3)
    return x_3, y_4


def RK4(x_0: float, y_0: float, dt: float, F: Callable) -> Tuple[float]:
    k1 = K(y_0, x_0, F)
    x_0 += dt
    k2 = K(k1, x_0, F)
    x_0 += dt
    k3 = K(k2, x_0, F)
    return k1, k2, k3


def K(curr_y: float, x_0: float, F: Callable) -> float:
    k1 = F(x_0, curr_y)
    k2 = F(x_0 + (dt / 2), curr_y + (dt * k1) / 2)
    k3 = F(x_0 + (dt / 2), curr_y + (dt * k2) / 2)
    k4 = F(x_0 + dt, curr_y + dt * k3)
    return curr_y + (dt / 6) * (k1 + 2 * k2 + 2 * k3 + k4)


print("V0......................:", v_0)
print("Y0......................:", y_0)
print("T0......................:", t_0)
adams_bashforth(0, v_0, y_0, dt, F)
