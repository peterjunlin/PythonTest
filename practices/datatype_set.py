def set_initialization():
    set1 = {1, 2, 3}
    assert type(set1) == set

    set1 = set([1, 2, 3])
    assert type(set1) == set

    set1 = set('hello world')
    assert set1 == {'h', 'd', 'r', 'l', 'o', 'e', ' ', 'w'}


def set_operations():
    set1 = {1, 2, 3}

    # Append element to set.
    set1.add(4)
    assert set1 == {1, 2, 3, 4}

    # Repeated value has no effect
    set1.add(1)
    assert set1 == {1, 2, 3, 4}

    # element order in set is not significant
    assert {'l', ' ', 'w', 'o', 'h', 'r'} == {' ', 'l', 'w', 'o', 'h', 'r'}

    set2 = {3, 4, 5, 6}
    set3 = set1 | set2
    assert set3 == {1, 2, 3, 4, 6, 5}

    set3 = set1 & set2
    assert set3 == {3, 4}

    set3 = set1 - set2
    assert set3 == {1, 2}

    set3 = set1 ^ set2
    assert set3 == {1, 2, 5, 6}


def set_comprehension():
    set1 = {x for x in 'hello world' if x not in 'abcdefg'}
    assert set1 == {'l', ' ', 'w', 'o', 'h', 'r'}


if __name__ == '__main__':
    set_initialization()
    set_operations()
    set_comprehension()
