import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix
import traceback

def main():
    try:
        u = Matrix([
            [1., -1.],
            [-1., 1.],
        ])
        print("det(u) :", u.determinant())
        print("*********************************")
        
        
        v = Matrix([
            [1., 2., 3.],
            [4., 5., 6.],
            [7., 8., 9.],
        ])
        print("det(v):", v.determinant())
        print("*********************************")
        
        w = Matrix([
            [2., 0., 0.],
            [0., 2., 0.],
            [0., 0., 2.],
        ])
        print("det(w):", w.determinant())
        print("*********************************")
        
        
        y = Matrix([
            [8., 5., -2.],
            [4., 7, 20.],
            [7., 6., 1.],
        ])
        print("det(y):", y.determinant())
        print("*********************************")
        x = Matrix([
            [8., 5., -2., 4.],
            [4., 2.5, 20., 4.],
            [8., 5., 1., 4.],
            [28., -4., 17., 1.]
        ])
        print("det(x):", x.determinant())

    except ValueError as e:
        print(f"Error: {e}")
        traceback.print_exc()
        

if __name__ == "__main__":
    main()