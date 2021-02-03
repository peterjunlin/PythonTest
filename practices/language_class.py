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

    print("This line is at the end of class definition. "
          "This line will run too, without need to create an instance.")


class Polygon(Shape):
    print("Polygon class loading.")
    _abc_ = 0
    __def = 0

    def __init__(self):
        self.x = 0
        print(dir())

    def func1(self):
        self.x = 1
        print('In func1()')

    def func2(self):
        x = 2
        self.func1()

    def func3(self):
        print(dir(self))  # this can display the mingled double underscore name _A__def


if __name__ == "__main__":
    print("After this line, create an instance of Shape class.")
    e = Shape()
    p = Polygon()

    # print(type(e))
    # print(isinstance(e, Shape))
    Shape.method1()  # access class-member
    e.member1 = 20  # access instance-member variable
    e.method1()
    e.method2()

