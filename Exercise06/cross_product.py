import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix
from Exercise05.cosine import angle_cos as cosine
from typing import TypeVar, Generic, List


import numpy as np
f32 = np.float32
K = TypeVar('K')

def cross_product(u: Vector[K], v: Vector[K]) -> Vector[K]:
    if u.size() != 3 or v.size() != 3:
        raise Exception("vector not 3-dimensional")
    return Vector([
        u[1]*v[2] - u[2]*v[1],
        u[2]*v[0] - u[0]*v[2],
        u[0]*v[1] - u[1]*v[0]
    ])


def main():
    try:
        u = Vector([0., 0., 1.])
        v = Vector([1., 0., 0.])
        print(cross_product(u, v))

        u = Vector([1., 2., 3.])
        v = Vector([4., 5., 6.])
        print(cross_product(u, v))

        u = Vector([4., 2., -3.])
        v = Vector([-2., -5., 16.])
        print(cross_product(u, v))


    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()