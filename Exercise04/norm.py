from typing import TypeVar, Generic, List, Type
import numpy as np

K = TypeVar('K')
f32 = np.float32




def Norm(cls: Type['Vector[K]']) -> Type['Vector[K]']:
    def norm_1(self) -> f32:
        sum = 0
        for vec in self.vec:
            sum += vec if vec >= 0 else -vec
        return sum

    def norm(self) -> f32:
        sum = 0
        for vec in self.vec:
            sum += (vec if vec >= 0 else -vec) ** 2
        return sum ** 0.5

    def norm_inf(self) -> f32:
        return max([vec if vec >= 0 else -vec for vec in self.vec])

    for name, method in [("norm", norm), ("norm_1", norm_1), ("norm_inf", norm_inf)]:
        if not hasattr(cls, name):
            setattr(cls, name, method)

    return cls