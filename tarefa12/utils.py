from typing import List, Tuple
import numpy as np


def LU(M: List[List[float]]) -> Tuple[List[List[float]], List[List[float]]]:
    M = np.array(M)
    L = np.identity(np.shape(M)[0])
    U = np.identity(np.shape(M)[0])

    for j in range(np.shape(M)[0]):
        for i in range(j + 1):
            value = 0
            for k in range(i):
                value = value + (L[i, k] * U[k, j])
            U[i, j] = M[i, j] - value

        for i in range(j + 1, np.shape(M)[0]):
            value = 0
            for k in range(j):
                value = value + (L[i, k] * U[k, j])
            if U[j, j] == 0:
                raise ValueError("Matriz não se decompõe em LU!")
            L[i, j] = (M[i, j] - value) / U[j, j]

    return (L.tolist(), U.tolist())


def resolution_LU(L: List[List[float]], U: List[List[float]], b: List[float]):
    L = np.array(L)
    U = np.array(U)
    b = np.array(b)

    y = np.zeros(np.shape(b))
    x = np.zeros(np.shape(b))
    size = np.shape(b)[0]

    for i in range(size):
        y[i] = b[i]
        for j in range(i):
            y[i] = y[i] - (L[i, j] * y[j])

    for i in range(size - 1, -1, -1):
        x[i] = y[i]
        for j in range(size - 1, i, -1):
            x[i] = x[i] - (U[i, j] * x[j])

        x[i] = x[i] / U[i, i]

    return x.tolist()


def dot_prod_vec(vec_a: List[float], vec_b: List[float]) -> List[float]:
    return sum([a * b for (a, b) in list(zip(vec_a, vec_b))])


def dot_prod_mat_x_vec(mat: List[List[float]], vec: List[float]) -> List[float]:
    if len(mat) != len(vec):
        raise Exception(
            f"Matriz de tamanho {len(mat)}x{len(mat[0])} e vetor de tamanho {len(vec)} não podem ser multiplicados."
        )

    n = len(vec)
    new_vec = [0] * n
    for i in range(n):
        sum_v = 0
        for j in range(n):
            sum_v += mat[i][j] * vec[j]
        new_vec[i] = sum_v

    return new_vec


def indentity(size: int) -> List[List[float]]:
    out = []
    for i in range(size):
        line = []
        for j in range(size):
            if i == j:
                line.append(1.0)
            else:
                line.append(0.0)
        out.append(line)
    return out


def normalize_vec(vec: List[float | int]) -> float:
    vec = list(map(lambda e: e * e, vec))
    return sum(vec) ** (0.5)


def unit_vec(vec: List[float | int]) -> List[float | int]:
    sum_m = normalize_vec(vec)
    return list(map(lambda e: e / sum_m, vec))


def print_mat(mat: List[List], label=None) -> None:
    if label is not None:
        print(label)

    for row in mat:
        line_str = "|"
        for e in row:
            if abs(e) < 1e-10:
                line_str += f" {0.0:^15.6} "
            else: 
                line_str += f" {float(e):^15.6} "
        line_str += "|"
        print(line_str)
