import os


def create_and_write_binary_file(filename):
    b = b'Hello World!'

    with open(filename, 'wb') as f:
        f.write(b)


def read_binary_file(filename):
    with open(filename, 'rb') as f:
        b = f.read()
        print(b)


if __name__ == '__main__':
    filename1 = './temp/test.bin'
    create_and_write_binary_file(filename1)
    read_binary_file(filename1)
