from typing import TypeVar, Generic, List, Type
import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))

K = TypeVar('K')

def Trace(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def trace(self) -> K:
        if not self.is_square():
            raise ValueError("Trace is only defined for square matrices.")
        trace = 0
        for i in range(self.shape()[0]):
            trace += self.matrix[i][i]
        return trace
    
    if not hasattr(cls, "trace"):
        setattr(cls, "trace", trace)
    return cls