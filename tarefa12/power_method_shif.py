from typing import List, Tuple
from power_method_inv import *
import numpy as np


def power_method_shiff(A: List[List[float]], v_0: List[float], ε: float, μ: float) -> Tuple[float, List[float]]:

    A = np.array(A) - (μ * np.identity(len(A)))
    λ, x = power_method_inv(A.tolist(), v_0, ε)
    λ_i = λ + μ
    x_i = x

    return λ_i, x_i
