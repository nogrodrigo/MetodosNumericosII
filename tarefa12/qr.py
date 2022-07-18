from math import inf
from typing import Tuple
from numpy.typing import NDArray
import numpy as np
from utils import print_mat, print_vec
from householder_method import householder_method


def QR_method(
    A: NDArray, eps: float = 1e-5, flag: bool = False
) -> Tuple[NDArray, NDArray]:
    L = inf
    A_old = A.copy()
    phi = np.identity(len(A))
    i = 0
    while L > eps:
        Q, R = QR(A_old)
        print_mat(Q.tolist(), f"Matriz Q na iteração {i}: ")
        print_mat(R.tolist(), f"Matriz R na iteração {i}: ")
        A_new = R @ Q
        A_old = A_new
        if flag:
            print_mat(A_new.tolist(), f"Matriz A_new na iteração {i}: ")
        phi = phi @ Q
        L = sum_of_squares(A_new)
        i += 1

    lamb = np.array([A_new[i, i] for i in range(len(A_new))])
    
    # Colocando na forma "padrão" (último elemento = 1)
    for i in range(len(A_new)):
        for j in range(len(A_new)):
            phi[i,j] /= phi[len(A_new)-1, j]
    
    return (phi, lamb)


def QR(A: NDArray) -> Tuple[NDArray, NDArray]:
    n = len(A)
    A_new = A.copy()
    QT = np.identity(n)
    for j in range(n - 1):
        A_old = A_new.copy()
        Hj = householder_hj(A_old, j)
        A_new = Hj @ A_old
        QT = Hj @ QT
        # print_mat(QT.tolist(), f"Matriz Q na iteração {j}: ")

    return (QT.transpose(), A_new)


def sum_of_squares(A: NDArray) -> float:
    n = len(A)
    L = 0
    for j in range(n - 1):
        for i in range(j + 1, n):
            L += (A[i, j]) ** 2

    return L


def householder_hj(A: NDArray, j: int) -> NDArray:
    """
    A: Matriz dada.
    j: Coluna da qual se deseja gerar a matriz de Householder.
    k: Dimensão da matriz.
    """
    size = len(A)
    # Inicializar vetores
    w = np.zeros(size)
    w_l = np.zeros(size)
    I = np.identity(size)

    # Copiar os elementos abaixo da diagonal da coluna j da matriz A
    # para as respectivas posições no vetor w, isto é, da posição j até o final.
    w[j:size] = A[j:size, j]
    # Calcular o comprimento do vetor w.
    l_w = np.linalg.norm(w)
    # Copiar l_w na posição j do vetor w′
    w_l[j] = l_w
    # Calcular o vetor N
    N = w - w_l
    # Normalizar o vetor N
    n_mod = np.linalg.norm(N)
    n = N / n_mod
    # n transposto.
    n_t = np.array([n]).transpose()
    # Montar a matriz de Householder
    Hj = I - 2 * n * n_t

    return Hj


A = np.array(
    [
        [40, 8, 4, 2, 1],
        [8, 30, 12, 6, 2],
        [4, 12, 20, 1, 2],
        [2, 6, 1, 25, 4],
        [1, 2, 2, 4, 5],
    ]
)

# 1)
phi, lamb = QR_method(A)
print_mat(phi.tolist(), "\n\nPhi:")
print_vec(lamb.tolist(), "\n\nLambda: ")
print(f"\nAutovalor 1: {lamb[0]}")
print_vec(phi[0 : len(A), 0].tolist(), "\nAutovetor 1:")
print(f"\nAutovalor 2: {lamb[1]}")
print_vec(phi[0 : len(A), 1].tolist(), "\nAutovetor 2:")
print(f"\nAutovalor 3: {lamb[2]}")
print_vec(phi[0 : len(A), 2].tolist(), "\nAutovetor 3:")
print(f"\nAutovalor 4: {lamb[3]}")
print_vec(phi[0 : len(A), 3].tolist(), "\nAutovetor 4:")
print(f"\nAutovalor 5: {lamb[4]}")
print_vec(phi[0 : len(A), 4].tolist(), "\nAutovetor 5:")

# 2)
print()
A_bar, H = householder_method(A)
phi, lamb = QR_method(A_bar, 1e-6, True)
print_mat(phi.tolist(), "\n\nPhi: ")
phi = H @ phi
for i in range(len(phi)):
        for j in range(len(phi)):
            phi[i,j] /= phi[len(phi)-1, j]
print_mat(phi.tolist(), "\n\nH * Phi: ")
