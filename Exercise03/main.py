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
    v = Vector([3., 2.])
    print(u.dot(v))


if __name__ == "__main__":
    main()