import sys


def practice1():
    s1 = input("Waiting for your input:")
    print("Your input is: ", s1)


def practice2():
    """ Count frequency of each line. 
    Use pipe to feed this routine.
    This can be used to count how many times the user have logged in.
    """
    names = {}
    for name in sys.stdin.readlines():
        name = name.strip()
        if name in names:
            names[name] += 1
        else:
            names[name] = 1
    for s1 in names.keys():
        print(s1, "->", names[s1])

