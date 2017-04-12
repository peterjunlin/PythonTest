def practice1():
    dict1 = {}
    print("type(dict1): ", type(dict1))
    dict1["a"] = 1
    print('dict1["a"] = 1   ', dict1)
    dict1["a"] += 1  # throw KeyError if the key does not exist
    print('dict1["a"] += 1   ', dict1)
    dict1["a"] = dict1.get("a", 0) + 1  # this won't throw exception if the key does not exist
    print('dict1["a"] = dict1.get("a", 0) + 1   ', dict1)
