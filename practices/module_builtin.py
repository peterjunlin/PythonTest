def builtins_names():
    list1 = dir('__builtins__')
    print(len(list1))
    print(list1)


if __name__ == '__main__':
    builtins_names()
