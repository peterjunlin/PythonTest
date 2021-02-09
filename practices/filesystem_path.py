import os


def filesystem_separator():
    # Path separator
    print("Path separator: ".format(os.path.sep))


def filesystem_special_path():
    # Path composing
    p = os.path.join("peter", "workspace")
    print(p)

    path1 = os.path.curdir
    print('Current working directory: {0}'.format(os.getcwd()))
    print('Current path = {0}'.format(os.curdir))
    print('Current path = {0}'.format(os.path.curdir))

    print('Absolute path = {0}'.format(os.path.abspath(path1)))
    print('Real path = {0}'.format(os.path.realpath(path1)))  # symbolic link to path


def filesystem_path_operations():
    filename = '/Users/peter/pythonStudy/practices/test.py'
    print('Split extension = {0}'.format(os.path.splitext(filename)))
    print('Split tail = {0}'.format(os.path.split(filename)))


if __name__ == '__main__':
    filesystem_separator()
    filesystem_special_path()
    filesystem_path_operations()
