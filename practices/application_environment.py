import sys


def interpreter_executable_path():
    print(sys.executable)


def python_version():
    print(sys.version_info)


def script_info():
    print(__name__)  # name of application main
    print(__file__)  # script file path


if __name__ == "__main__":
    interpreter_executable_path()
    python_version()
    script_info()
