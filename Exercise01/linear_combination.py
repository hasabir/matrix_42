import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from Exercise00.add_subtract_scale import Vector, Matrix
from typing import TypeVar, Generic, List
import numpy as np

f32 = np.float32

def linear_combination[K](u: List[Vector[K]], coefs: List[K]) -> Vector[K]:
    try:
        if u.size() != len(coefs):
            raise Exception("The two arrays provided as input are not of the same size")
        result = Vector([])
        for i in range(len(coefs)): #a × v1 + b × v2 ... + m × vn
            result.add(u[i].scl(coefs[i]))        

    except Exception as e:
        print(f"Error: {e}")


    return Vector(result)


def main():
    try:
        e1 = Vector([1., 0., 0.])
        e2 = Vector([0., 1., 0.])
        e3 = Vector([0., 0., 1.])
        
        
        v1 = Vector([1., 2., 3.])
        v2 = Vector([0., 10., -100.])
        

        print(linear_combination(Vector[f32]([v1, v2]), list[f32]([10., -2])))
        print(linear_combination(Vector[f32]([e1, e2, e3]), list[f32]([10., -2, 0.5])))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
