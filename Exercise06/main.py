from cross_product import cross_product
from vector import Vector
from matrix import Matrix


def main():
    try:
        u = Vector([0., 0., 1.])
        v = Vector([1., 0., 0.])
        print(cross_product(u, v))

        u = Vector([1., 2., 3.])
        v = Vector([4., 5., 6.])
        print(cross_product(u, v))

        u = Vector([4., 2., -3.])
        v = Vector([-2., -5., 16.])
        print(cross_product(u, v))


    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    main()