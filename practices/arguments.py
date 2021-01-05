import sys

def arguments1():
    print('Number of arguments: ', len(sys.argv))
    for i, s1 in enumerate(sys.argv):
        print(i, sys.argv[i])

def practice1():
    arguments1()
