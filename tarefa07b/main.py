from exp import *


print(gauss_hermite_4(-1, 1, lambda x: (1/(x**2)**(1/3)))) # OK
print(gauss_legendre_4(-1, 1, -1.2, 1.2, lambda x: (1/(x**2)**(1/3)))) # NO


print(gauss_hermite_4(-2, 0, lambda x: (1/(4 - x**2)**(1/2)))) # OK
print(gauss_legendre_2(-2, 0, -5, 5, lambda x: (1/(4 - x**2)**(1/2)))) # NO