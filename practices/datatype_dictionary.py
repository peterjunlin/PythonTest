def dict_initialization():
    # Set empty dictionary
    dict1 = dict()

    # Use constructor
    d = dict(a=1, b=2, c=3, d=4, e=5)

    # Use literal
    d = {'a':1, 'b':2}


def dict_properties():
    dict1 = dict(one=1)
    d = dict(a=1, b=2, c=3, d=4, e=5)

    # Get type of dictionary
    print("type(dict1): ", type(dict1))


def dict_operations():
    dict1 = dict{}

    # Add item and set value
    dict1["a"] = 1

    # Get value of an entry
    print('dict1["a"] = 1   ', dict1)

    # Change value of an entry
    dict1["a"] += 1  # throw KeyError if the key does not exist
    print('dict1["a"] += 1   ', dict1)

    dict1["a"] = dict1.get("a", 0) + 1  # this won't throw exception if the key does not exist
    print('dict1["a"] = dict1.get("a", 0) + 1   ', dict1)


if __name__ == "__main__":
    dict_initialization()
    dict_properties()
    dict_operations()
