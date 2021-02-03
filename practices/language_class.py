class Shape:
    """
    Find the executing sequence of each section of module and class.
    Find how to use class member variable in and out of class method and instance method.
    """
    member1 = 10
    print("This line is at the beginning of class definition, it will run when importing.")
    print("Only run once and this won't run in derived classes.")

    def __init__(self):
        print("Constructor")

    @classmethod
    def method1(cls):
        print('In class method, cls.member1 = ', cls.member1)  # access class-member variable

    def method2(self):
        print('In instance method, self.member1', self.member1)  # access instance-member variable

    print("This line run whenever the module loaded, no need to create an instance to run.")


class Polygon(Shape):
    print("Polygon class loading.")

    def __init__(self):
        self.x = 0  # Create and set member variable.
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

