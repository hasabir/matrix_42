from typing import Type, TypeVar, List

K = TypeVar('K', int, float)

def Inverse(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    
    def _adjoint(self):
        adjoint = [row.vec.copy() for row in self.matrix]
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix)):
                cofactor = (-1) ** (row + col)
                minor = cls(self._get_minor(self.matrix, row, col))
                adjoint[row][col] = cofactor * minor.determinant()
        return cls(adjoint).transpose()


    def inverse(self) -> Type['Matrix[k]']:
        adjoint = self._adjoint()
        det = self.determinant()
        if det == 0:
            raise Exception("Matrix is singular — and not invertible")
        return adjoint.scl(1 / det)
    
    
    for name, method in [("inverse", inverse), ("_adjoint", _adjoint)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls  