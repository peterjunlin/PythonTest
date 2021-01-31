dict1 = None


def show_vars():
    var1 = {'a': 10, 'b': 20}
    d1 = vars()
    print("vars(): ")
    arr1 = ['{0}:{1}'.format(x, y) for x, y in d1.items()]
    print("\n".join(arr1))


def show_locals():
    local1 = {'a': 10, 'b': 20}
    local2 = {'a': 10, 'b': 20}
    d1 = locals()
    print("locals(): ")
    arr1 = ['{0}:{1}'.format(x, y) for x, y in d1.items()]
    print("\n".join(arr1))


def show_globals():
    d1 = globals()
    print("globals(): ")
    print("\n".join(d1.keys()))
    # print(arr1)


def variable_info():
    s1 = """line 1
    line2
    line3
    """
    print("\nprint(s1)")
    print(s1)
    print("\nprint(repr(s1))")
    print(repr(s1))
    print("\nprint(ascii(s1))")
    print(ascii(s1))


def practice1():
    global dict1
    dict1 = {'a': 10, 'b': 20}  # this is global variable
    list1 = [1, 2, 3, 4, 5]  # this is local variable
    s1 = "abc"  # this is local variable
    show_vars()
    show_locals()
    show_globals()
    variable_info()


def del_variable():
    a = 10
    print("a is defined. a = 10")
    del a
    print("a is deleted. del a")
    try:
        print(a)
    except UnboundLocalError:
        print("Exception of UnboundLocalError: local variable 'a' referenced before assignment")


def practice2():
    # del_variable()
    d1 = dir(__builtins__)
    print(d1)
    print(len(d1))


class A:
    x = 10


def practice_equality():
    s1 = "abc"
    s2 = "abc"
    print('Compare two strings that has same value, s1 == s2  ', s1 == s2)  # True, compares the value
    print('Compare two strings that has same value, s1 is s2  ', s1 is s2)  # True, compares the memory address
    print(hex(id('abc')))
    print(hex(id(s1)))
    print(hex(id(s2)))

    a = A()
    b = A()
    print('Compare two instance of A(), a == b  ', a, b, a == b)  # False, compares the value  ????
    print('Compare two instance of A(), a is b  ', a is b)  # False, compares the address

    v1 = 123
    v2 = 122 + 1
    print('v1 == v2', v1 == v2)  # True, compare the value
    print('v1 is v2', v1 is v2)  # True, compare the address, immutable tend to use same address if same value
    print(hex(id(v1)))
    print(hex(id(v2)))

    x = [1, 2, 3]
    y = [1, 2, 3]
    print('Compare two identical lists, x == y  ', x == y)  # True, compare the value
    print('Compare two identical lists, x is y  ', x is y)  # False, compare the address
