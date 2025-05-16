import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '../')))
from vector import Vector
from matrix import Matrix



def main():
    u = Matrix([[1., 0.], [0., 1.]])
    v = Vector([4, 2])
    print(u.mul_vec(v))
    
    m = Matrix([[2., 0.], [0., 2.]])
    v = Vector([4, 2])
    print(m.mul_vec(v))

    m = Matrix([[2., -2.], [-2., 2.]])
    v = Vector([4, 2])
    print(m.mul_vec(v))
    
    m = Matrix([[2., 0.], [0., 2.]])
    v = Vector([4, 2])
    print(m.mul_vec(v))
    
    # m = Matrix([[1., 0.], [0., 2.]])
    # v = Vector([4, 2])
    # print(m.mul_vec(v))
    
    
    # m = Matrix([[2., 0.], [0., 2.]])
    # v = Vector([4, 2])
    # print(m.mul_vec(v))
    
    # m = Matrix([[2., 0.], [0., 2.]])
    # v = Vector([4, 2])
    # print(m.mul_vec(v))


if __name__ == "__main__":
    main()