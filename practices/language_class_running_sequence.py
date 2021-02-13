"""Sequence of class running."""


class Shape:
    print("Only run once as the class is imported, this won't run in derived classes, neither in instance.")

    def __init__(self):
        print("Constructor")

    @classmethod
    def method1(cls):
        print('Class method, cls.member1 = ', cls.member1)  # access class-member variable

    def method2(self):
        print('Instance method, self.member1', self.member1)  # access instance-member variable

    print("Only run once as the class is imported, this won't run in derived classes, neither in instance.")


class Polygon(Shape):
    print("Polygon class is loading.")

    def __init__(self):
        self.x = 0  # Create and set member variable.
        self.member1 = 0
        Shape.__init__(self)

    def to_set_member_variable(self):
        self.x = 1

    def to_call_member_function(self):
        self.to_set_member_variable()

    def to_set_inherited_member_variable(self):
        self.member1 = 567890


if __name__ == "__main__":
    print("After this line, create an instance of Shape class.")
    shape1 = Shape()
    polygon1 = Polygon()

    # print(type(e))
    # print(isinstance(e, Shape))
    Shape.method1()  # access class-member
    shape1.member1 = 20  # access instance-member variable
    shape1.method1()
    shape1.method2()

    print("\nPolygon inherited from Shape.")
    polygon1.member1 = 1234
    polygon1.method1()
    polygon1.method2()

    # Set member variable.
    polygon1.to_set_member_variable()
    print(polygon1.x)

    # Inherited instance member variable.
    polygon1.to_set_inherited_member_variable()
    print(polygon1.member1)

    # Inherited class member variable.
    print(Polygon.member1)

