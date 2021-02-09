def dict_initialization():
    # Set empty dictionary
    dict1 = dict()

    # With list of key-value pair
    dict1 = dict([('a', 1), ('b', 2), ('c', 3)])

    # Use keyword arguments
    d = dict(a=1, b=2, c=3, d=4, e=5)

    # Use literal
    d = {'a': 1, 'b': 2}


def dict_properties():
    dict1 = dict(one=1)
    d = dict(a=1, b=2, c=3, d=4, e=5)

    # Get type of dictionary
    assert type(dict1) == dict


def dict_operations():
    dict1 = dict()

    # Add item and set value
    dict1["a"] = 1  # Key is unique. If key exists, it will update the value.

    # Get value of an entry
    assert dict1["a"] == 1

    # Change value of an entry
    dict1["a"] += 1  # throw KeyError if the key does not exist
    assert dict1["a"] == 2

    dict1["a"] = dict1.get("a", 0) + 1  # this won't throw exception if the key does not exist
    assert dict1["a"] == 3

    dict2 = {'x': 1, 'y': 2, 'z': 3}
    dict3 = {**dict2, 'k': 4}  # unpacking dictionary
    assert dict3 == {'x': 1, 'y': 2, 'z': 3, 'k': 4}

    # find
    assert 'x' in dict2

    assert list(dict2.keys()) == ['x', 'y', 'z']
    assert list(dict2.values()) == [1, 2, 3]
    assert list(dict2.items()) == [('x', 1), ('y', 2), ('z', 3)]

    # Combine 2 lists as dictionary
    list1 = ['a', 'b', 'c']
    list2 = [1, 2, 3]
    dict1 = dict(zip(list1, list2))
    assert dict1 == {'a': 1, 'b': 2, 'c': 3}

    # order is not significant in dictionary
    assert {'a': 1, 'b': 2, 'c': 3} == {'a': 1, 'c': 3, 'b': 2}

    del dict1['a']
    assert dict1 == {'b': 2, 'c': 3}


def dict_comprehension():
    dict1 = {x: x**2 for x in [1, 2, 3]}
    assert dict1 == {1: 1, 2: 4, 3: 9}

    dict2 = {'a': 1, 'b': 2, 'c': 3}
    dict3 = {k: v*2 for (k, v) in dict2.items() if v < 3}
    assert dict3 == {'a': 2, 'b': 4}


def dict_looping():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    for k, v in dict1.items():
        dict1[k] = v * 2
    assert dict1 == {'a': 2, 'b': 4, 'c': 6}


if __name__ == "__main__":
    dict_initialization()
    dict_properties()
    dict_operations()
    dict_comprehension()
    dict_looping()
