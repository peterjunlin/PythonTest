def bytes_basics():
    # declare empty object
    b1 = bytes()
    print('b1 = bytes()\n', b1)
    # declare with size
    b2 = bytes(10)
    print('b2 = bytes(10)\n', b2)
    # declare bytes from other type
    b3 = bytes(range(10, 20, 2))
    print('b3 = bytes(range(10, 20, 2))\n', b3)

    # slice
    b4 = b3[0:3]
    print('b4 = b3[0:3]\n', b4)
    b5 = b3[-3:]
    print('b5 = b3[-3:]\n', b5)
    # assignment
    b6 = b3
    print('b6 = b3\n', b6)
    # get value
    try:
        a = b1[10]
    except IndexError as e:
        print('a = b1[10]', e)

    # judge empty bytes
    if (len(b1)==0):
        print('b1 is empty')
    else:
        print('b1 is not empty')

def practice1():
    bytes_basics()
