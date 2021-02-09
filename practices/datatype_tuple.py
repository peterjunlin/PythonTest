"""Note: tuple is immutable."""


def tuple_initialization():
    t = tuple([1, 2, 3])
    assert len(t) == 3

    t = tuple([[1, 2], [23, 14], [21, 20]])  # tuple that contains mutable objects.
    t[0].append(5)
    assert t[0] == [1, 2, 5]


def tuple_comprehension():
    t = tuple(x for x in range(10))
    assert t == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


def tuple_packing_unpacking():
    # tuple packing
    t = 1, 2, 3, 4
    assert t == (1, 2, 3, 4)

    # tuple unpacking
    x, y, z, a = t
    assert x == 1
    assert y == 2
    assert z == 3
    assert a == 4


if __name__ == "__main__":
    tuple_initialization()
    tuple_comprehension()
    tuple_packing_unpacking()
