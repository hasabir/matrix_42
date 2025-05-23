from typing import TypeVar, Generic, List
from Exercise00.add_subtract_scale import MatrixAddSubScl
from Exercise07.linear_map_matrix_multiplication import LinearMapMatrixMultiplication
from vector import Vector
from Exercise08.trace import Trace
from Exercise09.transpose import Transpose
from Exercise10.row_echelon_form  import RowEchelonForm

K = TypeVar('K')

@Trace
@Transpose
@MatrixAddSubScl
@RowEchelonForm
@LinearMapMatrixMultiplication
class Matrix(Generic[K]):
    def __init__(self, matrix: List[List[K]]):
        # self.matrix = matrix
        self.matrix = [Vector(vec) for vec in matrix]
        self.rows = len(matrix)
        self.columns = len(matrix[0]) if matrix else 0

    def __str__(self) -> str:
        matrix = [vector.vec for vector in self.matrix]
        return "[" + ",\n ".join("[" + ", ".join(map(str, row)) + "]" for row in matrix) + "]"

    def shape(self):
        return (self.rows, self.columns)

    def is_square(self):
        print("is_square", self.rows, self.columns)
        
        return self.rows == self.columns
    
    def size(self):
        return self.rows * self.columns
    
    def print(self, can_print=True, matrix=None):
        print(matrix)
        if matrix is None:
            matrix = self.matrix
        matrix = [vector.vec for vector in matrix]
        matrix = "[" + ",\n ".join("[" + ", ".join(map(str, row)) + "]" for row in matrix) + "]"
        if can_print:
            print(matrix)
        return matrix


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
        return matrix
        # self.vmatrix = self._to_vector_list()
        