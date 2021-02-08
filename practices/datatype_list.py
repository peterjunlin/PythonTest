def list_initialization():
    list1 = [1, 2, 3, 4]
    assert len(list1) == 4

    list1 = [x for x in range(0, 5)]
    assert list1 == [0, 1, 2, 3, 4]


def list_operations():
    list1 = [1, 2, 3, 4]

    # reverse
    list2 = [i for i in reversed(list1)]
    assert list2 == [4, 3, 2, 1]

    # reindexing
    del list1[1]
    assert list1 == [1, 3, 4]

    # Expanding immutables
    list2 = [1, 2, 3] * 2
    assert list2 == [1, 2, 3, 1, 2, 3]

    # filter
    list2 = list(filter(lambda item: item > 2, list1))
    assert list2 == [3, 4]

    # map - apply function to each item in the list.
    list2 = list(map(lambda item: item * 2, list1))
    assert list2 == [2, 6, 8]


def list_slice():
    list1 = [1, 2, 3, 4, 5]
    list2 = [*list1[1:], list1[0]]  # unpacking list
    list1[1] = 9
    assert list1 == [1, 9, 3, 4, 5]
    assert list2 == [2, 3, 4, 5, 1]


def list_comprehension():
    list1 = [x for x in range(10)]
    assert list1 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    list_initialization()
    list_operations()
    list_slice()
    list_comprehension()
