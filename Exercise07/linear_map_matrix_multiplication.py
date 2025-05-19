from typing import TypeVar, Generic, List, Type
import numpy as np
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector

K = TypeVar('K')


def LinearMapMatrixMultiplication(cls: Type['Matrix[K]']):
    def mul_vec(self, v: 'Vector[K]') -> 'Vector[K]':
        if self.shape()[1] != v.shape()[0]:
            raise Exception("Matrix and vector are not the same shape")
        return Vector([Vector(row).dot(v) for row in self.get_rows()])
    
    
    def mul_mat(self, m: 'Matrix[K]') -> 'Matrix[K]':
        if self.shape()[1] != m.shape()[0]:
            raise Exception("Incompatible shapes for matrix multiplication")

        columns = m.get_columns()
        rows = self.get_rows()
        return cls([
            [Vector(row).dot(Vector(col)) for col in columns]
            for row in rows
        ])



    for name, method in [("mul_vec", mul_vec), ("mul_mat", mul_mat)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)
    return cls
    
