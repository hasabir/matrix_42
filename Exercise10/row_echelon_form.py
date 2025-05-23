from typing import TypeVar, Generic, List, Type

K = TypeVar('K')


def RowEchelonForm(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def row_echelon(self) -> 'Matrix[K]':
        #first row
        
        # j = 0
        
        i = 1
        matrix = self.matrix

        i = 1
        pivot = {'row': 0, 'column': 0}
        pivot = {0: 0}
        while i < self.rows:
            k = i + 1
            while matrix[i]._is_zero():
                print('all values in the row are zeros')
                if matrix[k]:
                    self.swap(i, k)
                    k += 1
                else:
                    break
            j = 0
            while j <= list(pivot)[-1] and j < self.columns:
                if matrix[i][j] != 0:
                    x = -matrix[i][j]/ matrix[pivot[i-1]][j]
                    print('x = ', x)
                    matrix[i - 1].scl(x)
                    matrix[i].sub(matrix[i - 1].scl(x))
                j += 1

            if  j < self.columns and self.matrix[i][j] == 0 and i < self.rows - 1:
                self.swap_rows(i, i + 1, matrix)
                j = 0
                i += 1
            else:
                pivot[i] = j
            break
                
        
        
        return  None
        # return self.print(can_print=False, matrix=matrix)
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
        
        
        