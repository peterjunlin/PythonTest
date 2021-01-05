import os
import sys

def dir1():
    list1 = dir()
    print("list1 = dir()")
    print(list1)
    print()
    list1 = dir(__builtins__)
    print("list1 = dir(__builtins__)")
    print(list1)
    print()

def practice1():
    dir1()
