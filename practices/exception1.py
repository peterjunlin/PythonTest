def exception1(option=0):
    try:
        print("try block")
        if option == 1:
            raise TypeError
        elif option == 2:
            raise IOError
    except TypeError:
        print("Caught TypeError")
    else:
        print("else block")
    finally:
        print("finally block")
    print("after finally")

def practice1():
    print("Case 1: exception does not happen")
    exception1(0)
    print()
    print("Case 2: exception happened and was caught")
    exception1(1)
    print()
    print("Case 3: exception happened and was not caught")
    # exception1(2)
