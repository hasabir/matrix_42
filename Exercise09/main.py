import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix



def main():
    m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    
    print(m.transpose())


if __name__ == "__main__":
    main()