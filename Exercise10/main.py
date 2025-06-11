import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix



def main():
    u = Matrix([[1., 0., 0.],
                [0., 1., 0.],
                [0., 0., 1.],])
    print(u.row_echelon())
    print("*******************************")


    u = Matrix([[1., 2.],
                [3., 4.],])
    print(u.row_echelon())
    print("*******************************")
    

    u = Matrix([[1., 2.],
                [2., 4.],])
    print(u.row_echelon())
    print("*******************************")
    

    
    u = Matrix([[8., 5., -2., 4., 28.],
                [4., 2.5, 20., 4., -4.],
                [8., 5., 1., 4., 17.],])
    print(u.row_echelon())
    print("*******************************")
    

if __name__ == "__main__":
    main()

