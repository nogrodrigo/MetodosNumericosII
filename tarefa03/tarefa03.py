from cmath import inf
from math import log2, sin
from unittest import case

# Exemplo de função
def f(x):
    return (sin(2 * x) + 4 * x ** 2 + 3 * x) ** 2

# Abordagem fechada
def trapezio(xi, xf):
    h = xf - xi
    return (h / 2) * (f(xi) + f(xf))

def simpson13(xi, xf):
    h = (xf - xi) / 2
    return (h / 3) * (f(xi) + 4 * f(xi + h) + f(xf))

def simpson38(xi, xf):
    h = (xf - xi) / 3
    return (3 * h / 8) * (f(xi) + 3 * f(xi + h) + 3 * f(xi + 2 * h) + f(xf))

def grau4Fechada(xi, xf):
    h = (xf - xi) / 4
    return (2 * h / 45) * (7 * f(xi) + 32 * f(xi + h) + 12 * f(xi + 2 * h) + 32 * f(xi + 3 * h) + 7 * f(xf)) 

# Abordagem aberta

def trapezioAberta(xi, xf):
    h = (xf - xi) / 3
    return (3 * h / 2) * (f(xi + h) + f(xi + 2*h))

def milne(xi, xf):
    h = (xf - xi) / 4
    return (4 * h / 3) * (2*f(xi + h) - f(xi + 2*h) + 2*f(xi + 3*h))

def grau3Aberta(xi, xf):
    h = (xf - xi) / 5
    return (5 * h / 24) * (11*f(xi + h) + f(xi + 2*h) + f(xi + 3*h) + 11*f(xi + 4*h))

def grau4Aberta(xi, xf):
    h = (xf - xi) / 6
    return (h / 10) * (33 * f(xi + h) - 42 * f(xi + 2 * h) + 78 * f(xi + 3 * h) - 42 * f(xi + 4 * h) + 33 * f(xi + 5 * h))

# Main
a = int(input("Digite o início do intervalo: "))
b = int(input("Digite o fim do intervalo: "))
print()
print("Abordagem fechada:")
for i in [trapezio, simpson13, simpson38, grau4Fechada]:
    N = 1
    if   i == trapezio:  print("Regra do Trapézio:")
    elif i == simpson13: print("Regra de Simpson 1/3")
    elif i == simpson38: print("Regra de Simpson 3/8")
    else:                print("Regra de grau 4")
    iOld = 0
    iNew = inf
    err  = inf
    while (err > 1e-6):
        iOld = iNew
        iNew = 0
        for j in range(N):
            iNew += i(a + j*(b-a)/N, a + (j+1)*(b-a)/N)
        err = abs((iNew - iOld) / iNew)
        N *= 2
    N //= 2
    print("Valor:", iNew, "\nNúmero de Iterações:", log2(N))
print()
print("Abordagem aberta:")
for i in [trapezioAberta, milne, grau3Aberta, grau4Aberta]:
    N = 1
    if   i == trapezioAberta:  print("Regra do Trapézio:")
    elif i == milne:           print("Regra de Milne")
    elif i == grau3Aberta:     print("Regra de grau 3")
    else:                      print("Regra de grau 4")
    iOld = 0
    iNew = inf
    err  = inf
    while (err > 1e-6):
        iOld = iNew
        iNew = 0
        for j in range(N):
            iNew += i(a + j*(b-a)/N, a + (j+1)*(b-a)/N)
        err = abs((iNew - iOld) / iNew)
        N *= 2
    N //= 2
    print("Valor:", iNew, "\nNúmero de Iterações:", log2(N))