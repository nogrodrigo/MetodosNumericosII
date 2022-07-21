from utils import *
from power_method import *


A1 = [[5, 2, 1], [2, 3, 1], [1, 1, 2]]

A2 = [
    [40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5],
]

A3 = [
    [-40, 8, 4, 2, 1],
    [8, -30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5],
]

""" eigenvalue, eigenvector = power_method(A1, [1] * 3, 1e-10)
print_mat(A1, label="Matriz A1:")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}") """

eigenvalue, eigenvector = power_method(A3, [1] * 5, 1e-10)
print_mat(A3, label="Matriz A2:")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}")


""" last = eigenvector[-1]
print(last)
for i in range(len(eigenvector)):
    eigenvector[i] /= last

print_mat(A3, label="Matriz A2:")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}") """
