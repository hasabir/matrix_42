import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))

from Exercise00.add_subtract_scale import Vector, Matrix
from typing import TypeVar, Generic, List
import numpy as np
f32 = np.float32
V = TypeVar('V')




def lerp(u: V, v: V, t: f32) -> V:

    if type(u).__name__ == 'Vector' or type(u).__name__ == 'Matrix':
        return u.scl(1 - t).add(v.scl(t))
    return round(u * (1 - t) + t * v, 1)

def main():
    print(lerp(0., 1., 0.))
    print(lerp(0., 1., 0.5))
    print(lerp(21., 42., 0.3))
    print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
    print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20.,10.], [30., 40.]]), 0.5))


if __name__ == "__main__":
    main()