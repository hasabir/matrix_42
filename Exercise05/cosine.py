import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix
from typing import TypeVar, Generic, List


import numpy as np
f32 = np.float32
K = TypeVar('K')

def angle_cos(u: Vector[K], v: Vector[K]) -> f32:
    if not u or not v:
        raise ZeroDivisionError("Zero Division Error")
    u_norm = u.norm()
    v_norm = v.norm()
    if u_norm == 0 or v_norm == 0:
        raise ZeroDivisionError("Zero Division Error")
    return u.dot(v) / (u_norm * v_norm)
