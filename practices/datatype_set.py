def set_initialization():
    set1 = {1, 2, 3}
    assert type(set1) == set

    set1 = set([1, 2, 3])
    assert type(set1) == set


def set_operations():
    set1 = {1, 2, 3}

    # Append element to set.
    set1.add(4)
    assert set1 == {1, 2, 3, 4}

    # Repeated value has no effect
    set1.add(1)
    assert set1 == {1, 2, 3, 4}


if __name__ == '__main__':
    set_initialization()
    set_operations()
