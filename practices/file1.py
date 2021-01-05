import os

def read_and_display_text_file(filename):
    print("------ Read and display file", filename)
    with open(filename, 'r') as f:
        s = f.read()
        # s = f.readlines()
        print(s)
    f.close()

def write_text_file(filename):
    s1 = os.path.splitext(filename)[0]
    if not os.path.exists(s1):
        os.makedirs(s1)
    print("------ Write text file: ", filename)
    f = open(filename, 'w')
    f.write('Hello world!\n')
    f.write('How are you?\n')
    f.close()

def file_attributes(filename):
    print("------ File attributes")
    f = open(filename, 'r')
    len1 = f.tell()
    print("File length: {0}".format(len1))
    f.close()

def path_1(filename):
    print('------ path')
    print('os.path.realpath("{0}") = {1}'.format(filename, os.path.realpath(filename)))
    print('os.path.splitext("{0}") = {1}'.format(filename, os.path.splitext(filename)))
    print('os.path.abspath("{0}") = {1}'.format(filename, os.path.abspath(filename)))
    print('Current working directory: {0}'.format(os.getcwd()))
    print('Current working directory: {0}'.format(os.curdir))
    print(os.path.split(filename))
    print(os.path.split(os.path.splitext(filename)[0])[1])

def practice1():
    filename = './temp/test.txt'
    write_text_file(filename)
    read_and_display_text_file(filename)
    file_attributes(filename)
    path_1(filename)

