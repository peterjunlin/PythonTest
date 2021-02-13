class Shape:
    shape_cls_member = 1

    def __init__(self):
        self.shape_instance_member = 2

    @classmethod
    def shape_class_method(cls):
        print('Shape class method. Class member = ', cls.shape_cls_member)

    def shape_instance_method(self):
        self.shape_cls_member = 3


if __name__ == "__main__":
    shape1 = Shape()
    shape2 = Shape()

    # class member variable is instantiated in instance
    print("shape1 class member = ", shape1.shape_cls_member)
    shape1.shape_instance_method()
    print("=>shape1 class member = ", shape1.shape_cls_member)
    print("Shape class member = ", Shape.shape_cls_member)

    assert id(shape1.shape_cls_member) != id(shape2.shape_cls_member)

    # instance member variable
    print("shape1 instance member = ", shape1.shape_instance_member)
