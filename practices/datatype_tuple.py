def tuple_comprehension():
    t = tuple(x for x in range(10))
    assert t == (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


if __name__ == "__main__":
    tuple_comprehension()
