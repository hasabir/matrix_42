import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix
import traceback

def main():
    try:



        u = Matrix([
            [1., 0., 0.],
            [0., 1, 0.],
            [0., 0., 1.],
        ])
        print("rank(u):\n", u.rank())

        v = Matrix([
            [1., 2., 0., 0.],
            [2., 4., 0., 0.],
            [-1., 2., 1., 1.],
        ])
        print("rank(v):\n", v.rank())

        y = Matrix([
            [8., 5., -2.],
            [4., 7, 20.],
            [7., 6., 1.],
            [21., 18., 7.],
        ])
        print("rank(y):\n", y.rank())


    except Exception as e:
        print(f"Error: {e}")
        # traceback.print_exc()
        

if __name__ == "__main__":
    main()