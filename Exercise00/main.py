import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), '../')))
from  vector import Vector
from matrix import Matrix


def main():
   try:
        print("Vector Operations:")
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        
        print(f"v1 = {v1.vec}")
        print(f"v2 = {v2.vec}")
        
        v1.add(v2)
        print(f"{'*' * 20} v1 + v2 {'*' * 20}\nv1 = {v1}")
        
        v1.sub(v2)
        print(f"{'*' * 20} (v1 + v2) - v2 {'*' * 20} \nv1 = {v1}")
        
        v1.scl(2)
        print(f"{'*' * 20} 2 * v1  {'*' * 20}\nv1 = {v1}")
        
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
   except Exception as e:
       print(f"Error: {e}")


if __name__ == "__main__":
    main()
