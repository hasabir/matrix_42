import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix

import numpy as np

def main():
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(u.dot(v))

    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print(u.dot(v))

    u = Vector([-1., 6.])
    v = Vector([31., 2.])
    print(u.dot(v))
    print("********* numpy ************")
    print(np.dot(np.array([0., 0.]), np.array([1., 1.])))
    print(np.dot(np.array([1., 1.]), np.array([1., 1.])))
    print(np.dot(np.array([-1., 6.]), np.array([31., 2.])))


if __name__ == "__main__":
    main()