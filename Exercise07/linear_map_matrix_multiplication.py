from typing import TypeVar, Generic, List, Type
import numpy as np

K = TypeVar('K')


def LinearMapMatrixMultiplication(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def mul_vec(self, v: 'Vector[K]') -> 'Vector[K]':
        ...
    
    
    def mul_mat(self, m: 'Matrix[K]') -> 'Matrix[K]':
        ...
    
    for name, method in [("mul_vec", mul_vec), ("mul_mat", mul_mat)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)
    return cls
    
