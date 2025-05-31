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
        v = Matrix([
            [1., 2., 3.],
            [4., 5., 6.],
            [7., 8., 9.],
        ])
        print("det(v):", v.determinant())
        
        w = Matrix([
            [2., 0., 0.],
            [0., 2., 0.],
            [0., 0., 2.],
        ])
        print("det(w):", w.determinant())
        x = Matrix([
            [8., 5., -2., 4.],
            [4., 2.5, 20., 4.],
            [8., 5., 1., 4.],
            [28., -4., 17., 1.]
        ])
        print("det(x):", x.determinant())
        y = Matrix([
            [8., 5., -2.],
            [4., 7, 20.],
            [7., 6., 1.],
        ])
        print("det(y):", y.determinant())
        
        
        
        
        # mat4 = Matrix([
        # [1 + 1j,  2 - 2j,  0 + 3j, -1 + 0j],
        # [0 + 2j, -1 + 1j,  4 + 0j,  2 - 1j],
        # [3 + 0j,  0 - 1j, -2 + 2j,  1 + 1j],
        # [1 - 1j,  5 + 0j,  0 + 1j, -3 + 2j]
        # ])
        # det4 = mat4.determinant()
        # print("det(mat4):", det4)
        
    except Exception as e:
        print(f"Error: {e}")
        # traceback.print_exc()
        

if __name__ == "__main__":
    main()