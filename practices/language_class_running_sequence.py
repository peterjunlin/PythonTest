"""Sequence of class running."""


class Shape:
    print("Shape class is loading.")
    print("Only run once as the class is imported, this won't run in derived classes, neither in instance.")

    def __init__(self):
        print("Shape constructor")

    @classmethod
    def class_func(cls):
        print('Shape class method')

    def instance_func(self):
        print('Shape instance method')


class Polygon(Shape):
    print("Polygon class is loading.")

    def __init__(self):
        print("Polygon constructor")
        Shape.__init__(self)

    @classmethod
    def class_func(cls):
        print("Polygon class method")

    def instance_func(self):
        print("Polygon instance method")


if __name__ == "__main__":
    print("__main__ is running.")

    # Class method can be called without an instance.
    Shape.class_func()
    Polygon.class_func()

    shape1 = Shape()
    polygon1 = Polygon()

    shape1.instance_func()
    polygon1.instance_func()
