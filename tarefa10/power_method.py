from typing import List, Tuple
from math import inf
from utils import *


def power_method(A: List[List[float]], v_ini: List[float], eps: float) -> Tuple[float, List[float]]:

    λ_new = lamb_old = 0  # Step 2
    v_new = v_ini  # Step 3
    v_old = [0] * 3

    error = inf
    
    while error > eps:
        lamb_old = λ_new                      # Step 4
        v_old = v_new.copy()                  # Step 5
        v_old = unit_vec(v_old)               # Step 6
        v_new = dot_prod_mat_x_vec(A, v_old)  # Step 7
        λ_new = dot_prod_vec(v_old, v_new)    # Step 8
        error = abs(λ_new - lamb_old) / λ_new    # Step 9 - 10

    return λ_new, v_old
