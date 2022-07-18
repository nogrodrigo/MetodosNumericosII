from utils import *
from power_method_inv import *
from power_method_shif import *


A1 = [[5, 2, 1], [2, 3, 1], [1, 1, 2]]

A2 = [[-14, 1, -2], [1, -1, 1], [-2, 1, -11]]

A3 = [
    [40, 8, 4, 2, 1],
    [8, 30, 12, 6, 2],
    [4, 12, 20, 1, 2],
    [2, 6, 1, 25, 4],
    [1, 2, 2, 4, 5],
]

print(f"{'#' * 40} Potência inversa {'#' * 40}")

eigenvalue, eigenvector = power_method_inv(A1, [1] * 3, 1e-10)
print_mat(A1, label="Matriz A1:")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}\n\n")

eigenvalue, eigenvector = power_method_inv(A2, [1] * 3, 1e-10)
print_mat(A2, label="Matriz A2:")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}\n\n")  # resolver

eigenvalue, eigenvector = power_method_inv(A3, [1] * 5, 1e-10)
print_mat(A3, label="Matriz A3:")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}")

print("#" * 98)

print(f"{'#' * 35} Potência com deslocamento {'#' * 36}")

eigenvalue, eigenvector = power_method_shiff(A1, [1] * 3, 1e-10, 1.0)
print_mat(A1, label="Matriz A1:")
print("μ: 1.0")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}\n\n")


eigenvalue, eigenvector = power_method_shiff(A2, [1] * 3, 1e-10, -10.0)
print_mat(A2, label="Matriz A2:")
print("μ: 10.0")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}\n\n")  # resolver

eigenvalue, eigenvector = power_method_shiff(A3, [1] * 5, 1e-10, 3.0)
print_mat(A3, label="Matriz A3:")
print("μ: 3.0")
print(f"Autovalor: {eigenvalue}\nAutovetor: {eigenvector}")

print("#" * 98)
