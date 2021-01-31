import os
import sys


def test_builtins():
    list1 = dir()
    print("list1 = dir()")
    print(list1)
    print()
    list1 = dir(__builtins__)
    print("list1 = dir(__builtins__)")
    print(list1)
    print()


def test_environment_variable():
    s = "PATH"
    if s in os.environ:
        print(os.environ[s])
    else:
        print(s + ' does not exist.')
        print(os.environ)


def python_version():
    s1 = sys.version
    print(s1)


def script_file_path():
    print(__file__)


test_builtins()
test_environment_variable()
python_version()
script_file_path()
