from typing import Type, TypeVar, List

K = TypeVar('K', int, float)

def Determinant(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    
    def _get_sub_matrices(self, matrix):
        t = self.get_columns(matrix)
        if len(matrix[0]) == 3:
            return [
                cls([t[1][1:], t[2][1:]]).transpose(),
                cls([t[0][1:], t[2][1:]]).transpose(),
                cls([t[0][1:], t[1][1:]]).transpose()
            ]
        if len(matrix[0]) == 4:
            return [
                cls([t[1][1:], t[2][1:], t[3][1:]]).transpose(),
                cls([t[0][1:], t[2][1:], t[3][1:]]).transpose(),
                cls([t[0][1:], t[1][1:], t[3][1:]]).transpose(),
                cls([t[0][1:], t[1][1:], t[2][1:]]).transpose()
            ]
        return []

    def determinant(self) -> K:
        if not self.is_square():
            raise ValueError(f"Matrix {self.print(False)} is not a square matrix")
        if self.column_count > 4:
            raise NotImplementedError("Only matrices of dimension 4 or lower are supported")
        
        if self.column_count == 1:
            return self.matrix[0][0]

        def det_2(matrix):
            return (matrix[0][0] * matrix[1][1] -
                    matrix[1][0] * matrix[0][1])
        
        def det_3(matrix):
            sub_matrices = self._get_sub_matrices(matrix)
            
            return (
                matrix[0][0] * det_2(sub_matrices[0].matrix) -
                matrix[0][1] * det_2(sub_matrices[1].matrix) +
                matrix[0][2] * det_2(sub_matrices[2].matrix)
            )

        def det_4(matrix):
            sub_matrices = self._get_sub_matrices(matrix)
            return (
                matrix[0][0] * det_3(sub_matrices[0].matrix) -
                matrix[0][1] * det_3(sub_matrices[1].matrix) +
                matrix[0][2] * det_3(sub_matrices[2].matrix) -
                matrix[0][3] * det_3(sub_matrices[3].matrix)
            )


        if self.column_count == 2:
            return det_2(self.matrix)
        if self.column_count == 3:
            return det_3(self.matrix)
        if self.column_count == 4:
            return det_4(self.matrix)
        return None

    for name, method in [("determinant", determinant), ("_get_sub_matrices", _get_sub_matrices)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls
