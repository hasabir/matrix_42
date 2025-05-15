from matrix import Matrix
from typing import TypeVar, Generic, List
from Exercise00.add_subtract_scale import VectorAddSubScl
K = TypeVar('K')

@VectorAddSubScl
class Vector(Generic[K]):
    def __init__(self, vector: List[K]):
        self.vec = vector
    
    def __getitem__(self, i: int) -> K:
        return self.vec[i]
    
    def __str__(self) -> str:
        return str(self.vec)
        # return  "\n".join("[" + ", ".join(str(item)) + "]" for item in self.vec)

    def print(self):
        print(self.vec)
    
    def size(self):
        return len(self.vec)
    
    def shape(self):
        return f"({self.size()},)"
    
    def to_matrix(self, columns, rows):
        return Matrix([[self.vec[row + col * rows] for col in range(columns)] for row in range(rows)])
    
    

