from typing import Type, TypeVar, List

K = TypeVar('K', int, float)

def Inverse(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    
    
    def _adjoint(self, matrix):
        adjoint = matrix.copy()
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                cofactor = (-1)**(row + col)
                adjoint[row][col] = self.determinant()
    
    def inverse(self) -> Type['Matrix[k]']:
        ...
    
    
    for name, method in [("inverse", inverse)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls  