from typing import TypeVar, Generic, List

K = TypeVar('K')


class Matrix(Generic[K]):
    def __init__(self, matrix: List[List[K]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0]) if matrix else 0

    def __str__(self) -> str:
        return "[" + ",\n ".join("[" + ", ".join(map(str, row)) + "]" for row in self.matrix) + "]"

    def shape(self):
        return f"({self.rows}, {self.columns})"

    def is_square(self):
        return self.rows == self.columns

    def to_vector(self) -> List[K]:
        vec = []
        for i in range(self.columns):
            for j in range(self.rows):
                vec.append(self.matrix[j][i])
        return vec