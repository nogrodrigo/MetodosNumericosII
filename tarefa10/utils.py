from typing import List, Any

def transpose(mat: List[Any]):
    pass

def cross_prod(mat_a: List, mat_b: List):
    pass


def dot_prod_vec(vec_a: List[float], vec_b: List[float]) -> List[float]:
    return sum([a * b for (a, b) in list(zip(vec_a, vec_b))])


def dot_prod_mat_x_vec(mat: List[List[float]], vec: List[float]) -> List[float]:
    if len(mat) != len(vec):
        raise Exception(f"Matriz de tamanho {len(mat)}x{len(mat[0])} e vetor de tamanho {len(vec)} não podem ser multiplicados.")
    
    n = len(vec)
    new_vec = [0] * n
    for i in range(n):
        sum_v = 0
        for j in range(n):
            sum_v += mat[i][j] * vec[j]
        new_vec[i] = sum_v

    return new_vec

def normalize_vec(vec: List[float | int]) -> float:
    vec = list(map(lambda e: e * e, vec))
    return sum(vec)**(0.5)


def unit_vec(vec: List[float | int]) -> List[float|int]:
    sum_m = normalize_vec(vec)
    return list(map(lambda e: e / sum_m, vec))

def print_mat(mat: List[List], label=None) -> None:
    if label is not None:
        print(label)

    for row in mat:
        line_str = "|"
        for e in row:
            line_str += f" {e:^10.2f} "
        line_str += "|"
        print(line_str)