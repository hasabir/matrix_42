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

    for name, method in [("determinant", determinant), ("_get_minor", _get_minor)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls
