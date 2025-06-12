# from matrix import Matrix
from typing import TypeVar, Generic, List
from Exercise00.add_subtract_scale import VectorAddSubScl
from Exercise03.dot_product import DotProduct
from Exercise04.norm import Norm
K = TypeVar('K')

@VectorAddSubScl
@DotProduct
@Norm
class Vector(Generic[K]):
    def __init__(self, vector: List[K]):
        self.vec = vector
    
    def __getitem__(self, i: int) -> K:
        return self.vec[i]
    
    def __setitem__(self, i: int, item) -> None:
        self.vec[i] = item
    
    def __str__(self) -> str:
        return str(self.vec)
        # return  "\n".join("[" + ", ".join(str(item)) + "]" for item in self.vec)
    
    def __len__(self) -> int:
        return len(self.vec)

    def print(self):
        print(self.vec)
    
    def size(self):
        return len(self.vec)
    
    def shape(self):
        return (self.size(), )
    
    def _is_zero(self):
        for item in self.vec:
            if item != 0:
                return False
        return True
    
    def _copy(self):
        return Vector(list(self.vec).copy())
    

    # def to_matrix(self, columns, rows):
    #     return Matrix([[self.vec[row + col * rows] for col in range(columns)] for row in range(rows)])
    
    

