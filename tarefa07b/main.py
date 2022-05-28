from exp import *


print("Eq 0")
# print("Hermite: ")
# print(gauss_hermite_4(0, 1, lambda x: (1/(x)**0.5))) # OK
print("Legendre: ")
print(gauss_legendre_exp_simp_calculate(0, 1, -6, 6, lambda x: (1/(x)**0.5), num_p=4, eps=0.01)) # OK
print("==============================================")

print("Eq 1")
# print("Hermite: ")
# print(gauss_hermite_4(-1, 1, lambda x: (1/(x**2)**(1/3)))) # OK
print("Legendre: ")
print(gauss_legendre_exp_simp_calculate(-1, 1, -5, 5, lambda x: (1/(x**2)**(1/3)), num_p=4, eps=0.01)) # OK
print("==============================================")

print("Eq 2")
# print("Hermite: ")
# print(gauss_hermite_4(-2, 0, lambda x: (1/(4 - x**2)**(1/2)))) # OK
print("Legendre: ")
print(gauss_legendre_exp_simp_calculate(-2, 0, -8, 8, lambda x: (1/(4 - x**2)**(1/2)), num_p=4, eps=0.01)) # OK
