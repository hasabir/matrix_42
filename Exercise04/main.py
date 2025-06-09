import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../')))
from typing import TypeVar, Generic, List

from vector import Vector
from matrix import Matrix

import numpy as np

def main():
    u = Vector([0., 0., 0.])
    v = Vector([1., 2., 3.])
    w = Vector([-1., -2.])
    c = Vector([1 + 1j,  2 - 2j,  0 + 3j, -1 + 0j])

    print(f"u : norm_1 = {u.norm_1()} | norm = {u.norm()} | norm_inf = {u.norm_inf()}")
    print(f"v : norm_1 = {v.norm_1()} | norm = {v.norm()} | norm_inf = {v.norm_inf()}")
    print(f"w : norm_1 = {w.norm_1()} | norm = {w.norm()} | norm_inf = {w.norm_inf()}")
    print(f"c : norm_1 = {c.norm_1()} | norm = {c.norm()} | norm_inf = {c.norm_inf()}")

if __name__ == "__main__":
    main()