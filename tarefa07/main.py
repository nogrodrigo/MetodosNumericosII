from math import fabs, inf, isinf, isnan
from exp import gauss_legendre_exp_simp_calculate

eps = 1e-6

print("Gauss-Legendre com exponenciação simples: ")

a = float(input("Início do intervalo: "))
b = float(input("Fim do intervalo:"))

num_p = int(input("Quantidade de pontos de Legendre: "))
ci = float(input("Valor do corte inicial: "))

