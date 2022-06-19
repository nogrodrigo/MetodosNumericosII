from typing import Tuple
import numpy as np
from numpy.typing import NDArray
from power_method import power_method
from power_method_inv import power_method_inv
from power_method_shif import power_method_shiff
from utils import print_mat, print_vec


def householder_mat(A: NDArray, i: int) -> NDArray:
    size = len(A)
    # Inicializar vetores
    w = np.zeros(size)
    w_l = np.zeros(size)
    I = np.identity(size)

    # Copiar os elementos abaixo da diagonal da coluna i da matriz A
    # para as respectivas posições no vetor w, isto é, da posição i+1 até o final.
    w[i+1:size] = A[i+1:size, i]
    # Calcular o comprimento do vetor w.
    l_w = sum(list(map(lambda x: x * x, w)))**0.5
    # Copiar l_w na posição i+1 do vetor w′
    w_l[i+1] = l_w
    # Calcular o vetor N
    N = w - w_l
    # Normalizar o vetor N
    n_mod = sum(list(map(lambda x: x * x, N)))**0.5
    n = N / n_mod
    # n transposto
    n_t = np.array([n]).transpose()
    # Montar a matriz de Householder
    H = I - 2 * n * n_t

    return H

def householder_method(A: NDArray) -> Tuple[NDArray, NDArray]:
    n = len(A)
    H = np.identity(n)
    A_prev = A.copy()
    for i in range(n-2):
        # Construção da matriz de Householder do passo i.
        H_i = householder_mat(A_prev, i)
        # Transformação de similaridade do passo i.
        A_curr = H_i.transpose() @ A_prev @ H_i
        # Salvar para o próximo passo.
        A_prev = A_curr.copy()
        # Acumular o produto das matrizes de Householder.
        H = H @ H_i

    return (A_prev, H)


A1 = np.array(
    [[40, 8, 4, 2, 1],
     [8, 30, 12, 6, 2],
     [4, 12, 20, 1, 2],
     [2, 6, 1, 25, 4],
     [1, 2, 2, 4, 5]])

# Implemente o método de Householder e aplique-o sobre A para encontrar a matriz tridiagonal e a matriz acumulada H.
print("Implemente o método de Householder e aplique-o sobre A para encontrar a matriz tridiagonal e a matriz acumulada H.")
A_bar, H = householder_method(A1)
print_mat(A_bar.tolist(), "A barra: ")
print_mat(H.tolist(), "H: ")

# Use os métodos da potência para encontrar os autovalores e autovetores da matriz A barra.
print("\nUse os métodos da potência para encontrar os autovalores e autovetores da matriz A barra.")
eigenvalue_1, eigenvector_1 = power_method(A_bar.tolist(), [1.0] * 5, 1e-10)
eigenvalue_2, eigenvector_2 = power_method_shiff(A_bar.tolist(), [1.0] * 5, 1e-10, 33)
eigenvalue_3, eigenvector_3 = power_method_shiff(A_bar.tolist(), [1.0] * 5, 1e-10, 20)
eigenvalue_4, eigenvector_4 = power_method_shiff(A_bar.tolist(), [1.0] * 5, 1e-10, 10)
eigenvalue_5, eigenvector_5 = power_method_inv(A_bar.tolist(), [1.0] * 5, 1e-10)

print(f"Autovalor 1 de A barra: {eigenvalue_1}")
print(f"Autovalor 2 de A barra: {eigenvalue_2}")
print(f"Autovalor 3 de A barra: {eigenvalue_3}")
print(f"Autovalor 4 de A barra: {eigenvalue_4}")
print(f"Autovalor 5 de A barra: {eigenvalue_5}")
print_vec(eigenvector_1, "Autovetor 1 de A barra:")
print_vec(eigenvector_2, "Autovetor 2 de A barra:")
print_vec(eigenvector_3, "Autovetor 3 de A barra:")
print_vec(eigenvector_4, "Autovetor 4 de A barra:")
print_vec(eigenvector_5, "Autovetor 5 de A barra:")
# Usando a matriz H e os autovetores da matriz A barra encontre os autovetores da matriz A.
print("\nUsando a matriz H e os autovetores da matriz A barra encontre os autovetores da matriz A.")
print_vec((np.array(eigenvector_1).transpose() @ H).tolist(), "Autovetor 1 de A: ")
print_vec((np.array(eigenvector_2).transpose() @ H).tolist(), "Autovetor 2 de A: ")
print_vec((np.array(eigenvector_3).transpose() @ H).tolist(), "Autovetor 3 de A: ")
print_vec((np.array(eigenvector_4).transpose() @ H).tolist(), "Autovetor 4 de A: ")
print_vec((np.array(eigenvector_5).transpose() @ H).tolist(), "Autovetor 5 de A: ")
# Encontre os autovalores da matriz A.
print("\nEncontre os autovalores da matriz A.")
eigenvalue_1, eigenvector_1 = power_method(A1.tolist(), [1.0] * 5, 1e-10)
eigenvalue_2, eigenvector_2 = power_method_shiff(A1.tolist(), [1.0] * 5, 1e-10, 33)
eigenvalue_3, eigenvector_3 = power_method_shiff(A1.tolist(), [1.0] * 5, 1e-10, 20)
eigenvalue_4, eigenvector_4 = power_method_shiff(A1.tolist(), [1.0] * 5, 1e-10, 10)
eigenvalue_5, eigenvector_5 = power_method_inv(A1.tolist(), [1.0] * 5, 1e-10)
print(f"Autovalor 1 de A: {eigenvalue_1}")
print(f"Autovalor 2 de A: {eigenvalue_2}")
print(f"Autovalor 3 de A: {eigenvalue_3}")
print(f"Autovalor 4 de A: {eigenvalue_4}")
print(f"Autovalor 5 de A: {eigenvalue_5}")
print_vec(eigenvector_1, "Autovetor 1 de A:")
print_vec(eigenvector_2, "Autovetor 2 de A:")
print_vec(eigenvector_3, "Autovetor 3 de A:")
print_vec(eigenvector_4, "Autovetor 4 de A:")
print_vec(eigenvector_5, "Autovetor 5 de A:")