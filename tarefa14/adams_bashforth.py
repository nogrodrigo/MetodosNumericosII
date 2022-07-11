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
dt = 0.01


""" def adams_bashforth(
    k1: float,
    k2: float,
    k3: float,
    k4: float,
    dt: float,
    F: Callable,
) -> float:
    x_0 = 0

    _y_0 = F(x_0, k1)
    x_1 = x_0 + dt
    _y_1 = F(x_1, k2)
    x_2 = x_1 + dt
    _y_2 = F(x_2, k3)
    x_3 = x_2 + dt
    _y_3 = F(x_3, y_3)
    print("Valores de Y' calculados: ", _y_0, _y_1, y_2, _y_3)
    # Predição
    _y_4 = y_3 + ((dt / 24) * ((55 * _y_3) - (59 * _y_2) + (37 * _y_1) - (9 * _y_0)))
    print("Predição de Y...........: ", _y_4)
    # Recalculando y'4 com o valor encontrado na predição.
    # y'4 = F(v, y'4)
    #         ^-------- O valor que estamos tentando aproximar.
    # _y_4 = F(v, _y_4)
    # Correção
    y_4 = y_3 + ((dt / 24) * (9 * _y_4 + 19 * _y_3 - 5 * _y_2 + _y_1))
    print("Correção de Y...........: ", y_4)
    print("Valor de X..............: ", x_3)
    return x_3, y_4 """


""" 
def RK4(x_0: float, y_0: float, dt: float, F: Callable) -> Tuple[float]:
    k1 = K(y_0, x_0, F)
    x_0 += dt
    k2 = K(k1, x_0, F)
    x_0 += dt
    k3 = K(k2, x_0, F)
    return k1, k2, k3
 """


def sub_step(
    last_state: Tuple[float, float],
    dt: float,
) -> Tuple[Tuple[float, float, float, float]]:
    last_v, last_y = last_state

    v1 = -g - (k / m) * last_v
    v2 = -g - (k / m) * (last_v + (dt / 2))
    v3 = -g - (k / m) * (last_v + (dt / 2))
    v4 = -g - (k / m) * (last_v + dt)
    v = last_v + (dt / 6) * (v1 + 2 * v2 + 2 * v3 + v4)
    print("Velocidade tá OK!")
    print("v: ", v1, v2, v3, v4)
    print("last_v: ", v)

    y1 = last_y
    y2 = last_y + (dt * last_v) / 2
    y3 = last_y + (dt * last_v) / 2
    y4 = last_y + (dt * last_v)
    print(last_y)
    y = last_y + ((dt / 6) * (y1 + (2 * y2) + (2 * y3) + y4))
    print("Altura tá ERRADA!")
    print("y: ", y1, y2, y3, y4)
    print("last_y: ", y)

    return (v2, v3, v4, v), (y2, y3, y4, y)


def getSubstep(
    pastState: Tuple[float, float], dt: float, j: int
) -> Tuple[float, float]:
    vPast, yPast = pastState
    v = vPast + dt * (-g - k * vPast / m) / j
    y = yPast + dt * (vPast) / j
    print("v: ", v, "\ny: ", y)
    return (v, y)


sub_step((v_0, y_0), dt)
getSubstep((v_0, y_0), dt, 1)
