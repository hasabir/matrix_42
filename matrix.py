from typing import TypeVar, Generic, List
from Exercise00.add_subtract_scale import MatrixAddSubScl
from Exercise07.linear_map_matrix_multiplication import LinearMapMatrixMultiplication
from vector import Vector
K = TypeVar('K')

@MatrixAddSubScl
@LinearMapMatrixMultiplication
class Matrix(Generic[K]):
    def __init__(self, matrix: List[List[K]]):
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0]) if matrix else 0

    def __str__(self) -> str:
        return "[" + ",\n ".join("[" + ", ".join(map(str, row)) + "]" for row in self.matrix) + "]"

    def shape(self):
        return (self.rows, self.columns)

    def is_square(self):
        return self.rows == self.columns
    
    def size(self):
        return self.rows * self.columns
    

    def to_vector(self) -> List[K]:
        vec = []
        for i in range(self.columns):
            for j in range(self.rows):
                vec.append(self.matrix[j][i])
        return Vector(vec)
    
    def get_columns(self) -> List[List[K]]:
        vec = []
        for i in range(self.columns):
            column = [self.matrix[j][i] for j in range(self.rows)]
            vec.append(column)
        return vec

    def get_rows(self) -> List[List[K]]:
        return self.matrix