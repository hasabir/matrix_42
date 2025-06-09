import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))

from vector import Vector
from matrix import Matrix
from typing import TypeVar, Generic, List
import warnings


import numpy as np
f32 = np.float32
V = TypeVar('V')



def lerp(u: V, v: V, t: f32) -> V:
    if t > 1 or t < 0:
        warnings.warn(f"\033[93m{t} must be real, and 0 ≤t ≤1  (t ∈[0; 1](⊂R))\033[00m")
    if type(u).__name__ == 'Vector' or type(u).__name__ == 'Matrix':
        return u.scl(1 - t).add(v.scl(t))
    return u * (1 - t) + t * v

