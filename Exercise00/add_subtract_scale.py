from typing import TypeVar, Generic, List

K = TypeVar('K')

class Vector(Generic[K]):
    def __init__(self, vector: 'Vector[K]'):
        self.vec = vector
    
    def __getitem__(self, i: int) -> List[K]:
        return self.vec[i]
    
    def __str__(self) -> str:
        return  "\n".join("[" + ", ".join(str(item)) + "]" for item in self.vec)
    
    def __repr__(self) -> str:
        return f"Vector({self.vec})"

    def add(self, v: 'Vector[K]') -> None:
        for i in range(len(self.vec)):
            self.vec[i] += v[i]
        
    def sub(self, v: 'Vector[K]') -> None:
        if len(v.vec) != len(self.vec):
            raise Exception("Different size vectors")
        for i in range(len(self.vec)):
            self.vec[i] -= v[i]
        
    
    def scl(self, a: K) -> None:
        for i in range(len(self.vec)):
            self.vec[i] *= a
    


class Matrix(Generic[K]):
    def __init__(self, matrix: List[List[K]]):
        self.matrix = matrix
    
    def __str__(self) -> str:
        return "[" + ",\n ".join("[" + ", ".join(map(str, row)) + "]" for row in self.matrix) + "]"
    
    def add(self, v: 'Matrix[K]') -> None:
        if len(self.matrix) != len(v.matrix):
            raise ValueError("Matrices must have same number of rows")
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(v.matrix[i]):
                raise ValueError("All rows must have same length")
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += v.matrix[i][j]

    def sub(self, v: 'Matrix[K]') -> None:
        if len(self.matrix) != len(v.matrix):
            raise ValueError("Matrices must have same number of rows")
        for i in range(len(self.matrix)):
            if len(self.matrix[i]) != len(v.matrix[i]):
                raise ValueError("All rows must have same length")
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += v.matrix[i][j]
    
    def scl(self, a: K):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] *= a


def main():
   try:
        print("Vector Operations:")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        
        print(f"v1 = {v1.vec}")
        print(f"v2 = {v2.vec}")
        
        v1.add(v2)
        print(f"{'*' * 20} v1 + v2 {'*' * 20}\n{v1}")
        
        v1.sub(v2)
        print(f"{'*' * 20} (v1 + v2) - v2 {'*' * 20} \n{v1}")
        
        v1.scl(2)
        print(f"{'*' * 20} 2 * v1  {'*' * 20}\n{v1}")
        
        print("\nMatrix Operations:")
        m1 = Matrix([[1, 2], [3, 4]])
        m2 = Matrix([[5, 6], [7, 8]])
        
        print(f"{'*' * 20}m1 {'*' * 20}\n{m1}")
        print(f"{'*' * 20}m2 = {'*' * 20}\n{m2}")
        
        m1.add(m2)
        print(f"{'*' * 20} m1 + m2 {'*' * 20}\n{m1}")
        
        m1.sub(m2)
        print(f"{'*' * 20} (m1 + m2) - m2 {'*' * 20}\n{m1}")
        
        m1.scl(3)
        print(f"{'*' * 20}3 * m1 {'*' * 20}\n{m1}")
   except Exception() as e:
       print(f"Error: {e}")


if __name__ == "__main__":
    main()


