from typing import TypeVar, Generic, List, Type

K = TypeVar('K')




def Determinant(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def detrminant(self) -> K:
        if not self.is_square():
            raise Exception(f"matrix {self.print(False)} is not a square matrix")
        if self.column_count > 4:
            raise Exception(f"Only matrixes of dimmention 4 or lower are accepted")
        if self.column_count == 1:
            return 1.
        det = lambda matrix : matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]
        if self.column_count == 2:
            return det(self.matrix)
    
    
    if not hasattr(cls, "determinant"):
        setattr(cls, "determinant", detrminant)
    return cls


