print("This line is at the beginning of the module, this will run at time when this module is imported.")
print("Once the module was imported, the later importation will be skipped.")

class Shape:
    """
    Find the executing sequence of each section of module and class.
    Find how to use class member variable in and out of class method and instance method.
    """
    member1 = 10
    print("This line is at the beginning of class definition, which will run.")
    print("Only run once and this won't run in derived classes")

    def __init__(self):
        print("Constructor")

    @classmethod
    def method1(cls):
        print('In class method, cls.member1 = ', cls.member1)  # access class-member variable

    def method2(self):
        print('In instance method, self.member1', self.member1)  # access instance-member variable

    print("This line is at the end of class definition.")

def practice1():
    print("After this line, create an instance of Shape class.")
    e = Shape()
    # print(type(e))
    # print(isinstance(e, Shape))
    Shape.method1()  # access class-member
    e.member1 = 20  # access instance-member variable
    e.method1()
    e.method2()

class A:
    _abc_ = 0
    __def = 0

    def __init__(self):
        self.x = 0

    def func1(self):
        self.x = 1
        print('In func1()')

    def func2(self):
        x = 2
        self.func1()

    def func3(self):
        print(dir(self))  # this can display the mingled double underscore name _A__def

class B(Shape):
    print("Is this line run if create no instance -- yes!")

def practice2():
    k = A()
    k._abc_ = 1
    # k.__def = 1
    k.func3()
