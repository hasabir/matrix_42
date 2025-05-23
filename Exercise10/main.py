import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix



def main():
    m = [[4., 4.,-2., 2.],
         [0., 0., 0., 0.],
         [2., 9., -3., 8.],
         [6., 13., -1., 14]]
    
    m2 = [[0, -1, 3],
          [4., 0., 7.],
          [0., -1., 3]]
    
    m = Matrix(m)
    # m2 = Matrix(m2)

    print(f"matrix before row echelon form:\n{m}")
    print("*************************\n matrix after row echelon form:\n")
    print(m.row_echelon())


if __name__ == "__main__":
    main()
