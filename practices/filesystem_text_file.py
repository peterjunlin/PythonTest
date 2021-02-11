import os
from datetime import datetime


def write_text_file(filename):
    s1 = os.path.split(filename)[0]
    if not os.path.exists(s1):
        os.makedirs(s1)
    print("------ Write text file: ", filename)
    f = open(filename, 'w')
    f.write('Hello world!\n')
    f.write('How are you?\n')
    f.close()


def read_and_display_text_file(filename):
    print("------ Read and display file", filename)
    with open(filename, 'r') as f:
        s = f.read()
        # s = f.readlines()
        print(s)
    f.close()


def file_attributes(filename):
    print("------ File attributes")

    # Get size method 1 -- seek/tell
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)
    len1 = f.tell()
    print("File length in bytes: {0}".format(len1))
    f.close()

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
    read_and_display_text_file(filename1)
    file_attributes(filename1)
