def g():
    """customized generator"""
    print("1 is generated.")
    yield 1

    print("2 is generated.")
    yield 2

    print("3 is generated.")
    yield 3


def generator_for_generator_comprehension():
    # use customized generator in generator comprehension
    gen1 = g()
    m = max(x for x in gen1)
    assert m == 3

    # use range in generator comprehension
    m = max(x for x in range(10))
    assert m == 9


def generator_for_step_by_step():
    gen1 = g()
    print(type(gen1))
    a = gen1.__next__()
    print(a)
    a = gen1.__next__()
    print(a)
    a = gen1.__next__()
    print(a)


if __name__ == "__main__":
    generator_for_generator_comprehension()
    generator_for_step_by_step()
