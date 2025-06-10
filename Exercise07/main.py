import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix



def main():
    try:
        u = Matrix(
            [[1., 0.],
            [0., 1.]]
        )
        v = Vector([4., 2.])
        print(u.mul_vec(v))
        print("******************")
        
        
        u = Matrix(
            [[2., 0.],
            [0., 2.]]
        )
        v = Vector([4., 2.])
        print(u.mul_vec(v))
        print("******************")
        
        u = Matrix(
            [[2., -2.],
            [-2., 2.]]
        )
        v = Vector([4., 2.])
        print(u.mul_vec(v))
        print("***************** matrix multiplication ***************")
        
        u = Matrix(
            [[1., 0.],
            [0., 1.]]
        )
        v = Matrix(
            [[1., 0.],
            [0., 1.]]
        )
        print(u.mul_mat(v))
        print("******************")
        
        
        u = Matrix(
            [[1., 0.],
            [0., 1.]]
        )
        v = Matrix(
            [[2., 1.],
            [4., 2.]]
        )
        print(u.mul_mat(v))
        print("******************")
        u = Matrix(
            [[3., -5.],
            [6., 8.]]
        )
        v = Matrix(
            [[2., 1.],
            [4., 2.]]
        )
        print(u.mul_mat(v))
        print("******************")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()