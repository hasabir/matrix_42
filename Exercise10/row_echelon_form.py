from typing import TypeVar, Generic, List, Type

K = TypeVar('K')


def RowEchelonForm(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def row_echelon(self) -> 'Matrix[K]':
        pivot = {}
        i = 0
        j = 0
        matrix = self.matrix
        # matrix_columns = self.get_columns()
        # print("transpose", matrix_columns)
        for j in range(self.columns):
            i = 0
            while i < self.rows and i == 0:
                i += 1
            if i == 0 and i == self.rows:
                j += 1
        
        
        # while i < self.rows:
        #     next_row = i + 1
        #     while matrix[i]._is_zero() and next_row < self.rows:
        #         matrix = self.swap_rows(i, next_row, matrix)
        #         k += 1
        #     j = 0
        #     k = 0
        #     while j <= list(pivot)[-1] and j < self.columns:
        #         if matrix[i][j] != 0:
        #             x = -matrix[i][j]/ matrix[pivot[k]][j]
        #             matrix[i] =  matrix[i].add(matrix[k].scl(x))
        #         j += 1
        #         k += 1
                
        #     if  j < self.columns and self.matrix[i][j] == 0 and i < self.rows - 1:
        #         matrix = self.swap_rows(i, i + 1, matrix)
        #     else:
        #         pivot[i] = j
        #         i += 1

        return self.print(can_print=False, matrix=matrix)
    if not hasattr(cls, "row_echelon"):
        setattr(cls, "row_echelon", row_echelon)
    
    return cls


# if m[0][0] == 1 continue
# if m[0][0] > 1 -> m[0] / m[0][0]
# if m[0][0] == 0 -> swap with an other row and repeat above

#! pivot = i posion j

# if m[n] = all zeroes and m[n + 1] not all zeros swap m[n] with m[n + 1]

# from 0 to i - 1 m[j][i] check if 0
# if not :
    # for i = currect position, j = 0 to pivot old pivo position:
        # if m[i][j] > 1:
        #     row * x* r[i - 1]
        # if m[i][j] == 1:
        #     row / m[i][j]
        # repeat
        
        
        