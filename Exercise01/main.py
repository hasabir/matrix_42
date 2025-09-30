from linear_combination import linear_combination
from vector import Vector
from matrix import Matrix
import numpy as np

f32 = np.float32

def main():
    try:
        e1 = Vector([1., 0., 0.])
        e2 = Vector([0., 1., 0.])
        e3 = Vector([0., 0., 1.])
        
        
        v1 = Vector([1., 2., 3.])
        v2 = Vector([0., 10., -100.])
        

        print(linear_combination(Vector[f32]([e1, e2, e3]), list[f32]([10., -2, 0.5])))
        print(linear_combination(Vector[f32]([v1, v2]), list[f32]([10., -2])))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
