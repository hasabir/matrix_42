from typing import TypeVar, Generic, List, Type

K = TypeVar('K')



def RowEchelonForm(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def row_echelon(self) -> 'Matrix[K]':
        matrix = self.matrix
        i = 0                # current pivot‐row
        column = 0           # current column index

        # Loop until we've either processed all rows or all columns
        while i < self.row_count and column < self.column_count:
            # 1) Find a nonzero entry in this column at or below row i
            j = i
            while j < self.row_count and matrix[j][column] == 0:
                j += 1

            # 2) If no pivot found in this column, move to next column
            if j == self.row_count:
                column += 1
                continue

            # 3) Swap row j into row i
            matrix = self.swap_rows(j, i, matrix)

            # 4) Scale row i so the pivot at (i, column) becomes 1
            pivot_val = matrix[i][column]
            matrix[i] = matrix[i].scl(1 / pivot_val)

            # 5) Eliminate all entries below the pivot in this column
            k = i + 1
            while k < self.row_count:
                factor = matrix[k][column]
                if factor != 0:
                    matrix[k] = matrix[k].add(matrix[i].scl(-factor))
                k += 1

            # 6) Move to the next pivot‐row and next column
            i += 1
            column += 1

        return self.print(can_print=False, matrix=matrix)

    if not hasattr(cls, "row_echelon"):
        setattr(cls, "row_echelon", row_echelon)

    return cls








# def RowEchelonForm(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
#     def row_echelon(self) -> 'Matrix[K]':
#         matrix = self.matrix
#         column = 0

#         # Find the first pivot column and swap
#         while column < self.column_count:
#             i = 0
#             while i < self.row_count and matrix[i][column] == 0:
#                 i += 1
#             if i < self.row_count:
#                 matrix = self.swap_rows(i, 0, matrix)
#                 matrix[0] = matrix[0].scl(1 / matrix[0][column])
#                 break
#             column += 1

#         if column == self.column_count:
#             return self.print(can_print=False, matrix=matrix)

#         print("***************** first row found **********************")
#         self.print(can_print=True, matrix=matrix)
#         print("*********************************************\n\n")
    

#         pivot = {0: column}
#         i = 1
#         print(f"pivot position{pivot}")
#         loop = -1
#         last_pivot = list(pivot.values())[-1]
#         while i < self.row_count:
#             next_row = i + 1
#             while matrix[i]._is_zero() and next_row < self.row_count:
#                 matrix = self.swap_rows(i, next_row, matrix)
#                 next_row += 1
#             if matrix[i]._is_zero():
#                 break

#             column, pivot_position = 0, 0
#             last_pivot = list(pivot.values())[-1]
            
#             # print(f"last pivot: {last_pivot}")
#             while column <= last_pivot and column < self.column_count and pivot_position < len(pivot):
#                 pivot_row = pivot[pivot_position]
#                 print(f"matrix[{i}] = {matrix[i]}]")
#                 if matrix[i][column] != 0 and matrix[pivot_row][column] != 0:
#                     factor = -matrix[i][column] / matrix[pivot_row][column]
#                     print(f"factor: {factor}")  
#                     matrix[i] = matrix[i].add(matrix[pivot_row].scl(factor))
#                 column += 1
#                 pivot_position += 1

#             # print(f"matrix[{i}] = {matrix[i]}]")
            
#             while column < self.column_count and matrix[i][column] == 0:
#                 # print(f"matrix[{i}][{column}] = {matrix[i][column]}")
#                 column += 1
            
#             pivot[i] = column
#             i += 1
#             # if column < self.column_count and matrix[i][column] == 0 and i < self.row_count - 1 and loop != i:
#             #     loop = i
#             #     matrix = self.swap_rows(i, i + 1, matrix)
#             #     print(f"matrix after swap: {matrix[i]}")
#             #     # break
#             # else:
#             #     print("\n\n")
#             #     print(f"matrix[{i}]= {matrix[i]}")
#             #     print(f"matrix[{i}][{column}] = {matrix[i][column]}")
#             #     print("loop: ", loop)
                
#             #     # while column < self.column_count and matrix[i][column] == 0:
#             #     #     column += 1
#             #     loop = 0
#             #     pivot[i] = column
#             #     print(pivot)
#         print("\n\n")
#         return self.print(can_print=False, matrix=matrix)

#     if not hasattr(cls, "row_echelon"):
#         setattr(cls, "row_echelon", row_echelon)

#     return cls






# def RowEchelonForm(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
#     def row_echelon(self) -> 'Matrix[K]':
#         matrix = self.matrix

#         print("\n\n")
        
#         column = 0
#         while column < self.column_count:
#             i = 0
#             while i < self.row_count and matrix[i][column] == 0:
#                 i += 1
#             if i < self.row_count:
#                 matrix = self.swap_rows(i, 0, matrix)
#                 break
#             column += 1
#         if column == self.column_count:
#             return self.print(can_print=False, matrix=matrix)
#         pivot = {0: column}
#         i = 1
#         while i < self.row_count:
#             next_row = i + 1
#             while matrix[i]._is_zero() and next_row < self.row_count: 
#                 matrix = self.swap_rows(i, next_row, matrix)
#                 next_row += 1
#             if matrix[i]._is_zero():
#                 break

#             column, pivot_position = 0, 0
#             last_pivot =  list(pivot.values())[-1]
#             while column <= last_pivot and column < self.column_count:
#                 if matrix[i][column] != 0:
#                     x = -matrix[i][column]/ matrix[pivot[pivot_position]][column]
#                     matrix[i] =  matrix[i].add(matrix[pivot_position].scl(x))
#                 column += 1
#                 pivot_position += 1

#             if  column < self.column_count and matrix[i][column] == 0 and i < self.row_count - 1:
#                 print("since i am here there is a problem")
#                 matrix = self.swap_rows(i, i + 1, matrix)
#             else:
#                 pivot[i] = column
#                 i += 1
#         print("\n\n")
#         return self.print(can_print=False, matrix=matrix)
#     if not hasattr(cls, "row_echelon"):
#         setattr(cls, "row_echelon", row_echelon)
    
#     return cls


        
        
        
        # print("***************** first row found **********************")
        # self.print(can_print=True, matrix=matrix)
        # print("*********************************************\n\n")
    
    
    
