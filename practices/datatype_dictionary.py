def practice1():
    dict_definition()


def dict_definition():
    # Set empty dictionary
    dict1 = {}

    # Get type of dictionary
    print("type(dict1): ", type(dict1))

    # Add item and set value
    dict1["a"] = 1

    # Get value of an entry
    print('dict1["a"] = 1   ', dict1)

    # Change value of an entry
    dict1["a"] += 1  # throw KeyError if the key does not exist
    print('dict1["a"] += 1   ', dict1)

    dict1["a"] = dict1.get("a", 0) + 1  # this won't throw exception if the key does not exist
    print('dict1["a"] = dict1.get("a", 0) + 1   ', dict1)


practice1()
