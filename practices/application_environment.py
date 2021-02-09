import sys
import os


def interpreter_executable_path():
    print("Python executable path = {0}".format(sys.executable))


def python_version():
    print(sys.version_info)


def script_info():
    assert __name__ == '__main__'
    print("script file path: {0}".format(__file__))


def os_environment():
    print("\nenviron['PYTHONPATH']: {}".format(os.environ['PYTHONPATH']))

    print("\nenviron['HOME']: {}".format(os.environ['HOME']))

    print("\nenviron.keys: ")
    print(list(os.environ.keys()))


def module_search_path():
    print("\n\nModule search path: ")
    for s in sys.path:
        print(s)


if __name__ == "__main__":
    interpreter_executable_path()
    python_version()
    script_info()
    os_environment()
    module_search_path()
