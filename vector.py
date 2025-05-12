from matrix import Matrix
from typing import TypeVar, Generic, List

K = TypeVar('K')


class Vector(Generic[K]):
    def __init__(self, vector: List[K]):
        # super().__init__(self)
        self.vec = vector
    
    def __getitem__(self, i: int) -> List[K]:
        return self.vec[i]
    
    def __str__(self) -> str:
        # return  "\n".join("[" + ", ".join(str(item)) + "]" for item in self.vec)
        return str(self.vec)

    def size(self):
        return len(self.vec)
    
    def shape(self):
        return f"({self.size()},)"
    
    def to_matrix(self, columns, rows):
        return Matrix([[self.vec[row + col * rows] for col in range(columns)] for row in range(rows)])
    

import numpy as np


# print(np.array([1, 2, 3]).shape)

u = Vector([1, 2, 3, 2])
print(u.shape())
# print(u.to_matrix(2, 2))
u = u.to_matrix(2, 2)

print(u)
print(u.shape())

print(u.is_square())

# u = Matrix(u)
# print(u)
print(u.to_vector())

# prin)


