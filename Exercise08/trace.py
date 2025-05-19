from typing import TypeVar, Generic, List, Type
import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))

K = TypeVar('K')

def Trace(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def trace(self) -> K:
        ...
    
    if not hasattr(cls, "trace"):
        setattr(cls, "trace", trace)
    return cls