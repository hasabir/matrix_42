import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix



def main():
    m = [[2., 4.,-2., 2.],
         [2., 9., -3., 8.],
         [-2., -3., 7., 10],
         [6., 13., -1., 14]]
    
    m2 = [[0, -1, 3],
          [4., 0., 7.],
          [0., -1., 3]]
    
    m = Matrix(m)
    # m2 = Matrix(m2)

    print(m.row_echelon())


if __name__ == "__main__":
    main()
