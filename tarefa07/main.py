from math import fabs, inf, isinf, isnan
from exp import gauss_legendre_exp_simp_calculate

eps = 1e-6

print("Gauss-Legendre com exponenciação simples: ")

a = float(input("Início do intervalo: "))
b = float(input("Fim do intervalo:"))

num_p = int(input("Quantidade de pontos de Legendre: "))
ci = float(input("Valor do corte inicial: "))

new_res = inf
prev_res = inf

c = ci
step = 0.1

err = inf

while err > eps:
    prev_res = new_res
    new_res = gauss_legendre_exp_simp_calculate(a, b, -c, c, num_p, lambda x: 1/(x**2)**(1/3), eps)
    c += step
    
    if isnan(new_res) or isinf(new_res):
        c = ci
        step /= 10
        new_res = inf
        continue
    
    err = fabs((new_res - prev_res) / new_res)

print(new_res)