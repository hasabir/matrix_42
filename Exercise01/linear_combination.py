import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix
from typing import TypeVar, Generic, List
import numpy as np

f32 = np.float32
K = TypeVar('K')

def linear_combination(u: List[Vector[K]], coefs: List[K]) -> Vector[K]:
    try:
        if u.size() != len(coefs):
            raise Exception("The two arrays provided as input are not of the same size")
        result = Vector([])
        for i in range(len(coefs)): #a × v1 + b × v2 ... + m × vn
            result.add(u[i].scl(coefs[i]))
        return result
    except Exception as e:
        print(f"Error: {e}")


    return Vector(result)


