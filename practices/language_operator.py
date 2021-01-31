def multi_assignment1():
    a, b = 1, 2
    print("a, b = 1, 2")
    print("a = ", a, "b = ", b)
    print()
    a, b = 1, (2, 3)
    print("a, b = 1, (2, 3)")
    print("a = ", a)
    print("b = ", b)
    print()
    e = _func1()
    print("e = _func1()")
    print("e = ", e)
    print()
    c, d = _func1()
    print("c, d = _func1()")
    print("c = ", c)
    print("d = ", d)
    print()


def _func1():
    return 1, [2, 3]


def key_value_assignment():
    dict1 = {"a": 1, "b": 2, "c": 3}
    for i, (k, v) in enumerate(dict1.items()):
        print("{},{},{}".format(i, k, v))


def practice1():
    multi_assignment1()
    key_value_assignment()
