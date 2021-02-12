import os
from datetime import datetime


def write_text_file(filename):
    # make dir if not exists
    s1 = os.path.split(filename)[0]
    if not os.path.exists(s1):
        os.makedirs(s1)

    # create and write text file
    print("------ Write text file: ", filename)
    with open(filename, 'w') as f:
        f.write('Hello world!\n')
        f.write('How are you?\n')


def read_all_at_once(filename):
    print("------ Read all at once", filename)
    with open(filename, 'r') as f:
        s = f.read()
        print(s)


def read_as_iterator(filename):
    print("------ Read as iterator", filename)
    with open(filename, 'r') as f:
        for line in f:
            print(line, end='')


def file_attributes(filename):
    print("------ File attributes")

    # Get size method 1 -- seek/tell
    with open(filename, 'r') as f:
        f.seek(0, os.SEEK_END)
        len1 = f.tell()
        print("File length in bytes: {0}".format(len1))

    # Get size method 2
    d = os.path.getsize(filename)
    assert len1 == d

    # Get size method 3
    s1 = os.stat(filename)
    assert len1 == s1.st_size

    # file attributes
    print("File creation time: {0}".format(
        datetime.fromtimestamp(s1.st_ctime).strftime("%A, %B %d, %Y %I:%M:%S")))


if __name__ == '__main__':
    filename1 = './temp/test.txt'
    write_text_file(filename1)
    read_all_at_once(filename1)
    read_as_iterator(filename1)
    file_attributes(filename1)
