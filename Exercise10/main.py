import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix



def main():
    m = [[0., 0.,0., 0.],
         [0., 0., 0., 0.],
         [2., 9., -3., 8.],
         [6., 13., -1., 14]]

    m1 = [[0., 0.,0., 0.],
         [0., 5., 4., 0.],
         [0., 0., 3., 0.],
         [0., 0., 0., 2.]]


    m2 = [[6, -2, 3],
          [4., 0., 7.],
          [5., 0., 7.],
          [0., -1., 3]]
    
    m3 = Matrix([[1, 2, 3, 4],
          [0, 0, 0, 0],
          [0, 0, 5, 6],
          [2, 5, 4, 5]])
    
#     u = Matrix([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.],[8., 7., 1., 4., 17.],]);
    u = Matrix([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.],[8., 5., 1., 4., 17.],[8., 7., 1., 4., 17.],])
    
    m = Matrix(m)
    m1 = Matrix(m1)
    m2 = Matrix(m2)
     
    print(f"matrix before row echelon form:\n{m3}")
    print("*************************\n matrix after row echelon form:\n")
#     print(m.row_echelon())
    print(u.row_echelon())
#     print(m2.row_echelon())


if __name__ == "__main__":
    main()
