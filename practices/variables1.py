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


def practice1():
    global dict1
    dict1 = {'a': 10, 'b': 20}  # this is global variable
    list1 = [1, 2, 3, 4, 5]  # this is local variable
    s1 = "abc"  # this is local variable
    show_vars()
    show_locals()
    show_globals()
