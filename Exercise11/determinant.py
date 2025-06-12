from typing import Type, TypeVar, List

K = TypeVar('K', int, float)

def Determinant(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:

    def _get_minor(self, matrix: List[List[K]], row: int, col: int) -> List[List[K]]:
        minor = []
        for i in range(len(matrix)):
            if i == row:
                continue
            new_row = []
            for j in range(len(matrix[i])):
                if j == col:
                    continue
                new_row.append(matrix[i][j])
            minor.append(new_row)
        return minor

    def determinant(self) -> K:
        if not self.is_square():
            raise ValueError(f"Matrix {self.print(False)} is not a square matrix")

        def _det(matrix: List[List[K]]) -> K:
            size = len(matrix)
            if size == 1:
                return matrix[0][0]
            if size == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

            result = 0
            for j in range(size):
                sign = 1 if j % 2 == 0 else -1
                element = matrix[0][j]
                minor = self._get_minor(matrix, 0, j)
                result += sign * element * _det(minor)
            return result

        return _det(self.matrix)
    
    def get_permutation_matrix(self, A):
        ...
    
    def determinant_v2(self) -> K:
        if not self.is_square():
            raise ValueError(f"Matrix {self.print(False)} is not a square matrix")
        matrix = self._copy()
        row_index, column_index, pivot = 0, 0, 0
        # upper_triangular = self.matrix._copy()
        while row_index < self.row_count and column_index < self.column_count:
            j = row_index
            while j < self.row_count and matrix[j][column_index] == 0:
                j += 1
            
            if j == self.row_count:
                column_index += 1
                continue
            
            if matrix[row_index][column_index] == 0:
                # matrix = 
                self.get_permutation_matrix(matrix)
            
             
            # pivot_val = matrix[row_index][column_index]
            # if j != row_index:
            #     print("Swapping rows", row_index, j)
            #     matrix = self.swap_rows(j, row_index, matrix)
            # print(matrix[])
            
            
            print(f"Pivot value at ({row_index}, {column_index}): {pivot_val}")
            # matrix[row_index].scl(1 / pivot_val)

            # for row in range(self.row_count):
            #     if row != row_index:
            #         factor = matrix[row][column_index] 
            #         if factor != 0:
            #             scaled_row = matrix[row_index]._copy()
            #             matrix[row] = matrix[row].sub(scaled_row.scl(factor))

            row_index += 1
            column_index += 1
        return cls(matrix)

    for name, method in [("determinant", determinant), ("_get_minor", _get_minor), ("determinant_v2", determinant_v2), ("get_permutation_matrix", get_permutation_matrix)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls
