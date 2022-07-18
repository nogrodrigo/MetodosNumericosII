# Usando como modelo os passos de desenvolvimento do método preditor-corretor de
# terceira ordem, desenvolva o método preditor-corretor de quarta ordem.
# Si+1 = Si + dt/24 * ( 55*Fi - 59*Fi-1 + 37*Fi-2 - 9*Fi-3 ) <- Predição
# Si+1 = Si + dt/24 * ( 9*Fi+1 + 19*Fi - 5*Fi-1 + Fi-2 ) <- Correção
from typing import Tuple


t_0 = 0
v_0 = 5
y_0 = 200
k = 0.25
m = 2
g = 10
dt = 0.1


def next_state(s1, s2, s3, s4, dt: float):
    v1, y1 = s1
    v2, y2 = s2
    v3, y3 = s3
    v4, y4 = s4

    _v1 = -g - (k / m) * v1
    _v2 = -g - (k / m) * v2
    _v3 = -g - (k / m) * v3
    _v4 = -g - (k / m) * v4

    _y1 = v1
    _y2 = v2
    _y3 = v3
    _y4 = v4

    # Predição
    v5 = v4 + ((dt / 24) * ((55 * _v4) - (59 * _v3) + (37 * _v2) - (9 * _v1)))
    # y5 = y4 + ((dt / 24) * ((55 * _y4) - (59 * _y3) + (37 * _y2) - (9 * _y1)))

    _v5 = -g - (k / m) * v5
    _y5 = v5

    # Correção
    _v5 = v4 + ((dt / 24) * (9 * _v5 + 19 * _v4 - 5 * _v3 + _v2))
    _y5 = y4 + ((dt / 24) * (9 * _y5 + 19 * _y4 - 5 * _y3 + _y2))

    return (_v5, _y5)


def sub_step(last_state: Tuple[float, float], dt: float) -> Tuple[float, float]:
    last_v, last_y = last_state

    v1 = -g - (k / m) * last_v
    v2 = -g - (k / m) * (last_v + (dt / 2))
    v3 = -g - (k / m) * (last_v + (dt / 2))
    v4 = -g - (k / m) * (last_v + dt)
    v = last_v + (dt / 6) * (v1 + (2 * v2) + (2 * v3) + v4)

    y1 = last_y
    y2 = last_y + (v1 * dt / 2)
    y3 = last_y + (v2 * dt / 2)
    y4 = last_y + (v3 * dt)
    y = last_y + ((dt / 6) * (y1 + (2 * y2) + (2 * y3) + y4))

    return (v, y)


# Runge-Kutta
v_1, y_1 = v_0 + (dt / 2) * (-g - k * v_0 / m), y_0 + (dt / 2) * v_0
v_2, y_2 = v_1 + (dt / 2) * (-g - k * v_1 / m), y_1 + (dt / 2) * v_1
v_3, y_3 = v_2 + dt * (-g - k * v_2 / m), y_2 + dt * v_2

s_0 = (v_0, y_0)
s_1 = (v_1, y_1)
s_2 = (v_2, y_2)
s_3 = (v_3, y_3)

for dt in [0.1, 0.01, 0.001, 0.0001]:

    ymax = y_0
    maxHeightTime = 0
    time = 0
    iter = 0
    v = v_0
    y = y_0
    s0, s1, s2, s3 = s_0, s_1, s_2, s_3
    while y > 0:
        iter += 1
        s4 = next_state(s0, s1, s2, s3, dt)
        s0, s1, s2, s3 = s1, s2, s3, s4
        v, y = s4
        if y > ymax:
            ymax = y
            maxHeightTime = t_0 + dt * iter
        if y <= 0:
            time += dt * iter
    print(
        "ymax:                \t"
        + str(ymax)
        + "\nTempo até ymax: \t"
        + str(maxHeightTime)
        + "\nVelocidade no Impacto: \t"
        + str(v)
        + "\nTempo até o Impacto: \t"
        + str(time)
        + "\n"
    )
