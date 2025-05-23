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
    
    u = Matrix([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.],[8., 7., 1., 4., 17.],])
    # u = Matrix([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.],[8., 5., 1., 4., 17.],[8., 7., 1., 4., 17.],])
    
    m = Matrix(m)
    m1 = Matrix(m1)
    m2 = Matrix(m2)
     
    # print(f"matrix before row echelon form:\n{m3}")
    print("*************************\n matrix after row echelon form:\n")
#     print(m.row_echelon())
    print(m.row_echelon())
#     print(m2.row_echelon())


if __name__ == "__main__":
    main()



# # import numpy as np
# # # Function to check if matrix is in REF

# # def is_row_echelon_form(matrix):
# #     if not matrix.any():
# #         return False

#     rows = matrix.shape[0]
#     cols = matrix.shape[1]
#     prev_leading_col = -1

#     for row in range(rows):
#         leading_col_found = False
#         for col in range(cols):
#             if matrix[row, col] != 0:
#                 if col <= prev_leading_col:
#                     return False
#                 prev_leading_col = col
#                 leading_col_found = True
#                 break
#         if not leading_col_found and any(matrix[row, col] != 0 for col in range(cols)):
#             return False
#     return True

# def find_nonzero_row(matrix, pivot_row, col):
#     nrows = matrix.shape[0]
#     for row in range(pivot_row, nrows):
#         if matrix[row, col] != 0:
#             return row
#     return None

# # Swapping rows so that we can have our non zero row on the top of the matrix
# def swap_rows(matrix, row1, row2):
#     matrix[[row1, row2]] = matrix[[row2, row1]]

# def make_pivot_one(matrix, pivot_row, col):
#     pivot_element = matrix[pivot_row, col]
#     matrix[pivot_row] /= pivot_element
#     # print(pivot_element)

# def eliminate_below(matrix, pivot_row, col):
#     nrows = matrix.shape[0]
#     pivot_element = matrix[pivot_row, col]
#     for row in range(pivot_row + 1, nrows):
#         factor = matrix[row, col]
#         matrix[row] -= factor * matrix[pivot_row]

# # Implementing above functions
# def row_echelon_form(matrix):
#     nrows = matrix.shape[0]
#     ncols = matrix.shape[1]
#     pivot_row = 0
# # this will run for number of column times. If matrix has 3 columns this loop will run for 3 times
#     for col in range(ncols):
#         nonzero_row = find_nonzero_row(matrix, pivot_row, col)
#         if nonzero_row is not None:
#             swap_rows(matrix, pivot_row, nonzero_row)
#             make_pivot_one(matrix, pivot_row, col)
#             eliminate_below(matrix, pivot_row, col)
#             pivot_row += 1
#     return matrix


# matrix = np.array([[8., 5., -2., 4., 28.],[4., 2.5, 20., 4., -4.],[8., 7., 1., 4., 17.],])
# print("Matrix Before Converting:")
# print(matrix)
# print()
# result = row_echelon_form(matrix)
# print("After Converting to Row Echelon Form:")
# print(result)
# if is_row_echelon_form(result):
#     print("In REF")
# else:
#     print("Not in REF--------------->")