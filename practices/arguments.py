import sys


def arguments1():
    # To access application arguments by using sys.argv.
    print('Number of arguments: ', len(sys.argv))
    for i, s1 in enumerate(sys.argv):
        print(i, sys.argv[i])


def optional_list_arguments(a, lst=[]):
    # Mutable optional default value is initialized once and shared in global scope.
    lst.append(a)
    print(lst)


def optional_int_arguments(a, b=10):
    # Immutable optional default value is initialized once and shared in global scope as well.
    b += a
    print(b)


# arguments1()
#
# optional_list_arguments(1)
# optional_list_arguments(2)
#
# optional_int_arguments(1)
# optional_int_arguments(1)


def practice1():
    arguments1()
