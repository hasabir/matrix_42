import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from typing import TypeVar, Generic, List, Type


import numpy as np
f32 = np.float32
K = TypeVar('K')


def Dot(cls: Type['Vector[K]']) -> Type['Vector[K]']:
    def dot(self, v: 'Vector[K]') -> K:
        if self.shape() != v.shape():
            raise Exception("Vectors are not the same shape")
        result = [self.vec[i] * v.vec[i] for i in range(v.size())]
        sum = 0
        for x in result:
            sum += x
        return sum
    cls.dot = dot
    return cls