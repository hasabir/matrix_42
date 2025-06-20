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
        print("invese(u):\n", u.inverse())
        
        v = Matrix([
            [2., 0., 0.],
            [0., 2, 0.],
            [0., 0., 2.],
        ])
        print("invese(v):\n", v.inverse())
        
        y = Matrix([
            [8., 5., -2.],
            [4., 7, 20.],
            [7., 6., 1.],
        ])
        print("invese(y):\n", y.inverse())
        
        
        

    except Exception as e:
        print(f"Error: {e}")
        # traceback.print_exc()
        

if __name__ == "__main__":
    main()