from typing import Type, TypeVar, List

K = TypeVar('K', int, float)

def Determinant(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:

    @classmethod
    def get_permutation_matrix(cls, A, column_index, row_index) -> 'Matrix[K]':
        P = cls([[1 if i == j else 0 for i in range(A.column_count)] for j in range(A.row_count)])
        pivot_index = row_index
        for i in range(row_index, A.row_count):
            if abs(A.matrix[i][column_index]) > abs(A.matrix[pivot_index][column_index]):
                pivot_index = i
        if pivot_index != row_index:
            P.swap_rows(pivot_index, row_index)
        return P


    def determinant(self) -> K:
        if not self.is_square():
            raise ValueError(f"Matrix {self.print(False)} is not a square matrix")
        row_index, column_index, pivot_times = 0, 0, 0
        upper = self._copy()
        while row_index < self.row_count and column_index < self.column_count:
            j = row_index
            while j < self.row_count and upper.matrix[j][column_index] == 0:
                j += 1
            
            if j == self.row_count:
                return 0.0
            
            if upper.matrix[row_index][column_index] == 0:
                upper = self.get_permutation_matrix(upper, column_index, row_index).mul_mat(upper)
                pivot_times += 1

            k = row_index + 1
            while k < self.row_count:
                if upper.matrix[k][column_index] != 0:
                    
                    factor = upper.matrix[k][column_index] / upper.matrix[row_index][column_index]
                    scaled_row = upper.matrix[row_index]._copy()
                    upper.matrix[k] = upper.matrix[k].add(scaled_row.scl(-factor))
                k += 1
            row_index += 1
            column_index += 1
        determinant = (-1) ** pivot_times
        for i in range(self.row_count):
            determinant *= upper.matrix[i][i]

        return determinant

    for name, method in [("determinant", determinant), ("get_permutation_matrix", get_permutation_matrix)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls
