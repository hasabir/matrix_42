
from linear_interpolation import lerp
from vector import Vector
from matrix import Matrix


import numpy as np
f32 = np.float32

def main():
    print(lerp(0., 1., 1.))
    print(lerp(0., 1., 2.5))
    print(lerp(21., 42., 0.3))
    print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
    print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20.,10.], [30., 40.]]), 0.5))


if __name__ == "__main__":
    main()