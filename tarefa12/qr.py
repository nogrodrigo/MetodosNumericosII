from math import inf
from re import X
from typing import Tuple
from numpy.typing import NDArray
import numpy as np
from utils import print_mat

def QR_method(A: NDArray, eps: float = 1e-5) -> Tuple[NDArray, NDArray]:
    L = inf
    A_new = A.copy()
    phi = np.identity(len(A))
    while L > eps:
        A_old = A_new
        Q, R = QR(A_old)
        A_new = R @ Q
        phi = phi @ Q
        L = sum_of_squares(A_new)
    
    lamb = np.array([A_new[i, i] for i in range(len(A_new))])
    return (phi, lamb)


def QR(A: NDArray) -> Tuple[NDArray, NDArray]:
    n = len(A)
    A_new = A.copy()
    QT = np.identity(n)
    for j in range(n-1):
        A_old = A_new.copy()
        Hj = householder_hj(A_old, j)
        A_new = Hj @ A_old
        QT = Hj @ QT
    
    return (QT.transpose(), A_new)


def sum_of_squares(A: NDArray) -> float:
    n = len(A)
    L = 0
    for j in range(n-1):
        for i in range(j+1, n):
            L += (A[i, j])**2

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
    [[40, 8, 4, 2, 1],
     [8, 30, 12, 6, 2],
     [4, 12, 20, 1, 2],
     [2, 6, 1, 25, 4],
     [1, 2, 2, 4, 5]])

phi, lamb = QR_method(A)
print_mat(phi.tolist(), "Phi:")
print(f"Lambda: {lamb.tolist()}")