def g():
    yield 1
    yield 2
    yield 3


def practice1():
    print("m = max(x for x in gen1)")
    gen1 = g()
    m = max(x for x in gen1)
    print(m)
