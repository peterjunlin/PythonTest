def list_operations():
    # reverse
    list1 = [1, 2, 3, 4]
    list2 = [i for i in reversed(list1)]
    print("{0} reversed: {1}".format(list1, list2))

    # reindexing
    print("list1[1] value before deleting: {0}".format(list1[1]))
    del list1[1]
    print("list1[1] value after deleting: {0}".format(list1[1]))

    # Expanding immutables
    list2 = [1, 2, 3] * 3
    print(list2)

    # Expanding referenced mutables
    list2 = [list1, list1, list1] * 3
    print(list2)
    list1[0] = 0
    print(list2)


def list_comprehension():
    list1 = [x for x in range(10)];
    assert list1 == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == "__main__":
    list_operations()
    list_comprehension()
