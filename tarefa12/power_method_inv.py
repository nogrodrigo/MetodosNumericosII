from typing import List, Tuple
from math import inf
from utils import *


def power_method_inv(A: List[List[float]], v_ini: List[float], eps: float) -> Tuple[float, List[float]]:

    L, U = LU(A)         # Step 2
    λ_new = lamb_old = 0 # Step 3
    v_new = v_ini        # Step 4
    v_old = [0] * 3      # Step 4

    error = inf
    
    while error > eps:
        lamb_old = λ_new                       # Step 5
        v_old = v_new.copy()                   # Step 6
        v_old = unit_vec(v_old)                # Step 7
        v_new = resolution_LU(L, U, v_old)     # Step 8
        λ_new = dot_prod_vec(v_old, v_new)     # Step 9
        error = abs((λ_new - lamb_old) / λ_new)  # Step 10

    λ_new = 1 / λ_new

    return λ_new, v_old
