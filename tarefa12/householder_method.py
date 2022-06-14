from copy import copy
import numpy as np
from numpy.typing import NDArray
from utils import print_mat

""" print(f"Vetor w: {w}")
    print(f"Vetor w': {w_l}")
    print(f"Vetor Lw: {l_w}")
    print(f"Vetor N: {N}")
    print(f"Vetor Módulo do N: {n_mod}")
    print(f"Vetor n: {n}")
    print(f"Vetor n_t: {n_t}")
    print(f"H3: {H}") """

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
    H = I - 2*n*n_t

    return H


def householder_method(A: NDArray):
    n = len(A)
    H = np.identity(n)
    A_prev = A.copy()
    A_curr = None
    # Construção da matriz de Householder do passo i.
    H_i = householder_mat(A_prev, 2)
    # Transformação de similaridade do passo i.
    A_curr = H_i * A_prev * H_i
    # Salvar para o próximo passo.
    A_prev = A_curr.copy()
    # Acumular o produto das matrizes de Householder.
    #H = H * H_i

    print_mat(A.tolist(), "A2:")
    print_mat(H_i.tolist(), "H3: ")
    print_mat(A_prev.tolist(), "A3:")



A = np.array(
    [[40, 8, 4, 2, 1],
     [8, 30, 12, 6, 2],
     [4, 12, 20, 1, 2],
     [2, 6, 1, 25, 4],
     [1, 2, 2, 4, 5]])


A_test = np.array(
    [[3, 1, 0, 0, 0],
     [1, 4, 3, 0, 0],
     [0, 3, 5, 2, 1],
     [0, 0, 2, 6, 3],
     [0, 0, 1, 3, 8]])

householder_method(A_test)
