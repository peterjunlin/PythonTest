class Shape:
    member1 = 10

    def __init__(self):
        print("Constructor")

    @classmethod
    def method1(cls):
        print('In class method, cls.member1 = ', cls.member1)

    def method2(self):
        print('In instance method, self.member1', self.member1)


def practice1():
    e = Shape()
    # print(type(e))
    # print(isinstance(e, Shape))
    Shape.method1()
    e.member1 = 20
    e.method1()
    e.method2()
