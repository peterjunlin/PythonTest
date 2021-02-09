def list_initialization():
    list1 = [1, 2, 3, 4]
    assert len(list1) == 4

    list1 = [x for x in range(0, 5)]
    assert list1 == [0, 1, 2, 3, 4]

    # unpacking
    list2 = [*list1]
    assert list2 == list1


def list_editing():
    list1 = [1, 2, 3]
    list2 = [4, 5, 4]

    list2.extend(list1)
    assert list2 == [4, 5, 4, 1, 2, 3]

    list2.append(5)
    assert list2 == [4, 5, 4, 1, 2, 3, 5]

    list2.insert(2, 9)
    assert list2 == [4, 5, 9, 4, 1, 2, 3, 5]

    assert list2.index(4) == 0  # find first matches

    list2.remove(4)  # remove first one found
    assert list2 == [5, 9, 4, 1, 2, 3, 5]

    k = list2.pop()  # pop last one
    assert list2 == [5, 9, 4, 1, 2, 3]
    assert k == 5

    list2.reverse()
    assert list2 == [3, 2, 1, 4, 9, 5]

    list3 = list2.copy()
    assert list2 == list3

    list3 = list2[:]
    assert list2 == list3


def list_operations():
    list1 = [1, 2, 3, 4]

    assert list1.count(4) == 1

    # reverse
    list2 = [i for i in reversed(list1)]
    assert list2 == [4, 3, 2, 1]

    # delete and reindexing
    del list1[1]
    assert list1 == [1, 3, 4]

    # Expanding immutables
    list2 = [1, 2, 3] * 2
    assert list2 == [1, 2, 3, 1, 2, 3]

    # Find
    assert 3 in list2

    # filter
    list2 = list(filter(lambda item: item > 2, list1))
    assert list2 == [3, 4]

    # map - apply function to each item in the list.
    list2 = list(map(lambda item: item * 2, list1))
    assert list2 == [2, 6, 8]

    assert [1, 2, 3] == [1, 3, 2]  # element order in list is significant


def list_slice():
    list1 = [1, 2, 3, 4, 5]
    list2 = [*list1[1:], list1[0]]  # unpacking list
    list1[1] = 9
    assert list1 == [1, 9, 3, 4, 5]
    assert list2 == [2, 3, 4, 5, 1]


def list_comprehension():
    list1 = [x for x in range(10)]
    assert list1 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    list2 = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    assert list2 == [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


if __name__ == "__main__":
    list_initialization()
    list_operations()
    list_slice()
    list_editing()
    list_comprehension()
