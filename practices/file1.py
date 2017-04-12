def read_and_display_text_file(filename):
    with open(filename, 'r') as f:
        s = f.read()
        # s = f.readlines()
        print(s)
    f.close()


def write_text_file(filename):
    f = open(filename, 'w')
    f.write('Hello world!\n')
    f.write('How are you?\n')
    f.close()


def practice1():
    filename = './temp/test.txt'
    print(">>>")
    print("Write text file")
    print("---")
    print(filename)
    write_text_file(filename)
    print(">>>")
    print("Read and display file")
    print("---")
    print(filename)
    print("---")
    read_and_display_text_file(filename)
