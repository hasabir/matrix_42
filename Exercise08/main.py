import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix
import traceback

def main():
    try:
        m = Matrix([[1, 2], [3, 4]])
        print(m.trace())
        m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        print(m.trace())
        m = Matrix([[1]])
        print(m.trace())
        m = Matrix([[1, 2], [3, 4], [5, 6]])
        print(m.trace())
        
        print("********************")
        
        u = Matrix([[1, 0], [0, 1]])
        print(u.trace())
        
        u = Matrix([
            [2., -5., 0.],
            [4., 3., 7.],
            [-2., 3., 4.],
            ])
        print(u.trace())
    except Exception as e:
        print(f"Error: {e}")
        # traceback.print_exc()
        

if __name__ == "__main__":
    main()