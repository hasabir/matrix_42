import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix
import traceback

def main():
    try:
        u = Matrix([
            [2, 3],
            [8, 9],
        ])
        print("det(u) :", u.determinant())

        
        
        
        

    except Exception as e:
        print(f"Error: {e}")
        # traceback.print_exc()
        

if __name__ == "__main__":
    main()