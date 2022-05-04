from cmath import exp, inf

def f(x):
    return ((exp(3*x) + 4*x**2) ** 0.5).real

def fDer(x, dx):
    return ((-1/4)*f(x - 2*dx) + 4*f(x - dx) - 15/2 * f(x) + 4*f(x + dx) - (1/4)*f(x + 2*dx)) / (3 * dx ** 2)

err = inf
x = 2
dx = 0.5

print("f(x) = ", f(x), '\n')
while (True):
    oldfDer = fDer(x, dx)
    print("deltax = ", dx, "\tf''(x) ~= ", oldfDer, "\te(x) = ", err)
    if (abs(err) <= 1e-5):
        break
    dx /= 2
    newfDer = fDer(x, dx)
    err = abs((newfDer - oldfDer) / newfDer)