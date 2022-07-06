from typing import Tuple

# PVI-2
t_0 = 0
v_0 = 5
y_0 = 200
k = 0.25
m = 2
g = 10

def getNextStateExplicit(pastState: Tuple[float, float], dt: float) -> Tuple[float,float]:
    vPast, yPast = pastState
    v = vPast + dt * (-g - k * vPast / m)
    y = yPast + dt * vPast
    return v, y

def getNextStateImplicit(pastState: Tuple[float, float], dt: float) -> Tuple[float, float]:
    vPast, yPast = pastState
    v = m * (vPast - g * dt) / (m + k * dt)
    y = yPast + m * dt * (vPast - g * dt) / (m + k * dt)
    return v, y

# Explícito
print("Euler Explícito:")
for dt in [0.1, 0.01, 0.001, 0.0001]:
    ymax = y_0
    maxHeightTime = 0
    time = 0
    y = y_0
    v = v_0
    iter = 0
    while y > 0:
        iter += 1
        v, y = getNextStateExplicit((v, y), dt)
        if y > ymax:
            ymax = y
            maxHeightTime = t_0 + dt * iter
        if y <= 0:
            time += dt * iter
    print("ymax:                \t"+str(ymax)+"\nTempo até ymax: \t"+str(maxHeightTime)+"\nVelocidade no Impacto: \t"+str(v)+"\nTempo até o Impacto: \t"+str(time)+"\n")

# Implícito
print("Euler Implícito:")
for dt in [0.1, 0.01, 0.001, 0.0001]:
    ymax = y_0
    maxHeightTime = 0
    time = 0
    y = y_0
    v = v_0
    iter = 0
    while y > 0:
        iter += 1
        v, y = getNextStateImplicit((v, y), dt)
        if y > ymax:
            ymax = y
            maxHeightTime = t_0 + dt * iter
        if y <= 0:
            time += dt * iter
    print("ymax:                \t"+str(ymax)+"\nTempo até ymax: \t"+str(maxHeightTime)+"\nVelocidade no Impacto: \t"+str(v)+"\nTempo até o Impacto: \t"+str(time)+"\n")