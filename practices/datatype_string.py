import sys


def string_functions():
    s1 = '  abc '
    s2 = 'hello'
    print("s1 = '", s1,"'")
    print("s1.strip() = '", s1.strip(), "'")
    print("s2.capitalize() = '", s2.capitalize(), "'")
    print("s1.find('a') = '", s1.find('a'),"'")
    it = reversed(s1)
    print(type(it))
    for i in it:
        # sys.stdout.write(i)
        print(i)


def practice1():
    string_functions()
