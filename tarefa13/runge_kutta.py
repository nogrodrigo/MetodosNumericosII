from typing import Tuple
from webbrowser import get

# PVI-2
t_0 = 0
v_0 = 5
y_0 = 200
k = 0.25
m = 2
g = 10

def getSubstep(pastState: Tuple[float, float], dt: float, j: int) -> Tuple[float, float]:
    vPast, yPast = pastState
    v = vPast + dt * (-g - k * vPast / m) / j
    y = yPast + dt * (vPast) / j
    return (v,y)

def getNextState(pastState: Tuple[float, float], dt: float) -> Tuple[float, float]:
    vPast, yPast = pastState
    subv1, suby1 = getSubstep(pastState, dt, 2)
    subv2, suby2 = getSubstep(pastState, dt, 1)
    v = vPast + dt * ((-g - k * vPast / m) / 6 + 4 * (-g - k * subv1 / m) / 6 + (-g - k * subv2 / m) / 6)
    y = yPast + dt * (vPast / 6 + 4 * subv1 / 6 + subv2 / 6)
    return (v,y)

for dt in [0.1, 0.01, 0.001, 0.0001]:
    ymax = y_0
    maxHeightTime = 0
    time = 0
    y = y_0
    v = v_0
    iter = 0
    while y > 0:
        iter += 1
        v, y = getNextState((v, y), dt)
        if y > ymax:
            ymax = y
            maxHeightTime = t_0 + dt * iter
        if y <= 0:
            time += dt * iter
    print("ymax:                \t"+str(ymax)+"\nTempo até ymax: \t"+str(maxHeightTime)+"\nVelocidade no Impacto: \t"+str(v)+"\nTempo até o Impacto: \t"+str(time)+"\n")