def set_functions():
    set1 = set([1, 2, 3])
    print("type(set1)", type(set1))
    set1.add(4)
    set1.add(1)  # repeat value has no effect
    print(set1)
    print()
    set2 = {'abc', 'def'}
    print(set2)
    print("type(set2)", type(set2))

def practice1():
    set_functions()
