from typing import TypeVar, Generic, List
from Exercise00.add_subtract_scale import MatrixAddSubScl
from Exercise07.linear_map_matrix_multiplication import LinearMapMatrixMultiplication
from vector import Vector
from Exercise08.trace import Trace
from Exercise09.transpose import Transpose
from Exercise10.row_echelon_form  import RowEchelonForm
from Exercise11.determinant import Determinant
from Exercise12.inverse import Inverse
from Exercise13.rank import Rank
K = TypeVar('K')

@Rank
@Trace
@Inverse
@Transpose
@Determinant
@RowEchelonForm
@MatrixAddSubScl
@LinearMapMatrixMultiplication
class Matrix(Generic[K]):
    def __init__(self, matrix: List[List[K]]):
        # self.matrix = matrix
        self.matrix = [Vector(vec) for vec in matrix]
        self.row_count = len(matrix)
        self.column_count = len(matrix[0]) if matrix else 0

    def __str__(self) -> str:
        matrix = [vector.vec for vector in self.matrix]
        return "[" + ",\n ".join("[" + ", ".join(map(str, row)) + "]" for row in matrix) + "]"

    def shape(self):
        return (self.row_count, self.column_count)

    def is_square(self):
        
        return self.row_count == self.column_count
    
    def size(self):
        return self.row_count * self.column_count
    
    def print(self, can_print=True, matrix=None):
        if matrix is None:
            matrix = self.matrix
        matrix = [vector.vec for vector in matrix]
        matrix = "[" + ",\n ".join("[" + ", ".join(map(str, row)) + "]" for row in matrix) + "]"
        if can_print:
            print(matrix)
        return matrix


    def to_vector(self) -> List[K]:
        vec = []
        for i in range(self.column_count):
            for j in range(self.row_count):
                vec.append(self.matrix[j][i])
        return Vector(vec)
    
    def get_columns(self, matrix=None) -> List[List[K]]:
        vec = []
        if matrix is None:
            matrix = self.matrix
        for i in range(len(matrix[0])):
            column = [matrix[j][i] for j in range(len(matrix))]
            vec.append(column)
        return vec
    
    # def _to_vector_list(self):
    #     return [Vector(vec) for vec in self.matrix]

    def get_rows(self) -> List[List[K]]:
        return self.matrix
    
    def swap_rows(self, row1, row2, matrix=None):
        if matrix is None:
            matrix = self.matrix
        stock = matrix[row1]
        matrix[row1] = matrix[row2]
        matrix[row2] = stock
        if matrix is None:
            self.matrix = matrix
        else:
            return matrix
        # self.vmatrix = self._to_vector_list()
    
    def _copy(self):
        for row in self.matrix:
            if not isinstance(row, Vector):
                raise TypeError("Matrix rows must be of type Vector")
        return Matrix([row._copy() for row in self.matrix])