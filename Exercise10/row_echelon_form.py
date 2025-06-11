from typing import TypeVar, Generic, List, Type

K = TypeVar('K')



def RowEchelonForm(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    
 
    def row_echelon(self) -> 'Matrix[K]':
        matrix = self.matrix
        row_index, column_index, old_pivot_row = 0, 0, None
        
        
        while row_index < self.row_count and column_index < self.column_count:
            j = row_index
            while j < self.row_count and matrix[j][column_index] == 0:
                j += 1
            
            if j == self.row_count:
                column_index += 1
                continue

            matrix = self.swap_rows(j, row_index, matrix)

            pivot_val = matrix[row_index][column_index]
            matrix[row_index].scl(1 / pivot_val)

            for row in range(self.row_count):
                if row != row_index:
                    factor = matrix[row][column_index] 
                    if factor != 0:
                        scaled_row = matrix[row_index]._copy()
                        matrix[row] = matrix[row].sub(scaled_row.scl(factor))

            row_index += 1
            column_index += 1
        return cls(matrix)

    if not hasattr(cls, "row_echelon"):
        setattr(cls, "row_echelon", row_echelon)


    return cls






