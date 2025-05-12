import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from Exercise00.add_subtract_scale import Vector
from typing import TypeVar, Generic, List

# K = TypeVar('K')


def linear_combination[K](u: List[Vector[K]], coefs: List[K]) -> Vector[K]:
    if len(u) != len(coefs):
        raise Exception("The two arrays provided as input are not of the same size")
    for i in range(len(coefs)):
        u[i].scl(coefs[i])
    
    
    return u


def main():
    e1 = Vector([1., 0., 0.])
    e2 = Vector([0., 1., 0.])
    e3 = Vector([0., 0., 1.])
    
    
    v1 = Vector([1., 2., 3.])
    v2 = Vector([0., 10., -100.])
    

    print(linear_combination([v1, v2], [10., -2]))
    # print(linear_combination([e1, e2, e3], [10., -2, 0.5]))


if __name__ == "__main__":
    main()
