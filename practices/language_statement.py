def test_del():
    # delete variable
    s = "abc"
    # del s[0] - this is not supported
    del s

    # delete element in list
    lst = [1, 2, 3, 4]
    del lst[0]  # [2, 3, 4]


def practice1():
    print("practice1 of statements")
    test_del()
