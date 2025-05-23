from typing import TypeVar, Generic, List, Type


K = TypeVar('K')

def VectorAddSubScl(cls: Type['Vector[K]']) -> Type['Vector[K]']:
    def add(self, v: 'Vector[K]') -> 'Vector[K]':
        if len(self.vec) == 0:
            self.vec = v.vec
        elif len(v.vec) != len(self.vec):
            raise Exception("Different size vectors")
        else:
            new_vec = self.vec
            for i in range(len(self.vec)):
                self.vec[i] += v[i]
        return cls(self.vec)

   
    def sub(self, v: 'Vector[K]') -> 'Vector[K]':
        if len(v.vec) != len(self.vec):
            raise Exception("Different size vectors")
        new_vec = self.vec
        for i in range(len(new_vec)):
            new_vec[i] -= v[i]
        return cls(new_vec)
        
    
    def scl(self, a: K) -> 'Vector[K]':
        new_vec = self.vec
        for i in range(len(new_vec)):
            new_vec[i] *= a
        return cls(new_vec)

    cls.add = add
    cls.sub = sub
    cls.scl = scl
    return cls

    


def MatrixAddSubScl(cls: Type['Matrix[K]']) -> Type['Matrix[K]']:
    def add(self, v: 'Matrix[K]') -> 'Matrix[K]':
        if len(self.matrix) != len(v.matrix):
            raise ValueError("Matrices must have same number of rows")
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(v.matrix[i]):
                raise ValueError("All rows must have same length")
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += v.matrix[i][j]
        return cls(self.matrix)

    def sub(self, v: 'Matrix[K]') -> 'Matrix[K]':
        if len(self.matrix) != len(v.matrix):
            raise ValueError("Matrices must have same number of rows")
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(v.matrix[i]):
                raise ValueError("All rows must have same length")
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += v.matrix[i][j]
        return cls(self.matrix)

    def scl(self, a: K) -> 'Matrix[K]':
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= a
        return cls(self.matrix)
    cls.add = add
    cls.sub = sub
    cls.scl = scl
    return cls







