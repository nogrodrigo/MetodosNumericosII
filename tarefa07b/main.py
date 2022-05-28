from exp import *


print("Eq 0")
# print("Hermite: ")
# print(gauss_hermite_4(0, 1,func=lambda x: (1/(x)**0.5))) # OK
print("Legendre: ")
print("Simples: ", gauss_legendre_exp_simp_calculate(0, 1, ci=-6, cf=6, func=lambda x: (1/(x)**0.5), num_p=4, eps=0.01)) # OK
print("Dupla: ", gauss_legendre_exp_doub_calculate(0, 1, ci=-2, cf=2, func=lambda x: (1/(x)**0.5), num_p=4, eps=0.01)) # OK
print("==============================================")

print("Eq 1")
# print("Hermite: ")
# print(gauss_hermite_4(-1, 1,func=lambda x: (1/(x**2)**(1/3)))) # OK
print("Legendre: ")
print("Simples: ", gauss_legendre_exp_simp_calculate(-1, 1, ci=-5, cf=5, func=lambda x: (1/(x**2)**(1/3)), num_p=4, eps=0.01)) # OK
print("Dupla: ", gauss_legendre_exp_doub_calculate(-1, 1, ci=-5, cf=5, func=lambda x: (1/(x**2)**(1/3)), num_p=4, eps=0.01)) # OK
print("==============================================")

print("Eq 2")
# print("Hermite: ")
# print(gauss_hermite_4(-2, 0,func=lambda x: (1/(4 - x**2)**(1/2)))) # OK
print("Legendre: ")
print("Simples: ", gauss_legendre_exp_simp_calculate(-2, 0, ci=-8, cf=8, func=lambda x: (1/(4 - x**2)**(1/2)), num_p=4, eps=0.01)) # OK
print("Dupla: ", gauss_legendre_exp_doub_calculate(-2, 0, ci=-1.65, cf=1.65, func=lambda x: (1/(4 - x**2)**(1/2)), num_p=4, eps=0.01)) # OK
