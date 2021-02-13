"""Sequence of try/except/else/finally"""


def exception1(option=0):
    try:
        print("try block")
        if option == 1:
            raise TypeError
        elif option == 2:
            raise IOError
    except TypeError:
        print("Caught TypeError.")
    else:
        print("Else block. This is only reached if no exception happens.")
    finally:
        print("Finally block. This is always reached no matter what happens.")
    print("After finally. This won't be reached if exception isn't caught.")


if __name__ == '__main__':
    print("Case 1: exception does not happen")
    exception1(0)
    print()
    print("Case 2: exception happened and was caught")
    exception1(1)
    print()
    print("Case 3: exception happened and was not caught")
    exception1(2)
