from cosine import angle_cos
from vector import Vector
from matrix import Matrix


def main():
    try:
        u = Vector([1., 0.])
        v = Vector([1., 0.])
        print(angle_cos(u, v))

        u = Vector([1., 0.])
        v = Vector([0., 1.])
        print(angle_cos(u, v))

        u = Vector([-1., 1.])
        v = Vector([1., -1.])
        print(angle_cos(u, v))

        u = Vector([2., 1.])
        v = Vector([4., 2.])
        print(angle_cos(u, v))

        u = Vector([1., 2., 3.])
        v = Vector([4., 5., 6.])
        print(angle_cos(u, v))

        # print(angle_cos(u, None))
        # print(angle_cos(u, Vector([0, 0])))
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()