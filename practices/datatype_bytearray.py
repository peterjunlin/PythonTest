"""bytearray is mutable."""


def bytearray_initialization():
    # declare empty bytearray
    b = bytearray()
    assert len(b) == 0

    # declare bytearray with size
    b = bytearray(2)
    assert b == bytearray(b'\00\00')

    # declare from string with encoding
    b = bytearray('abc', 'utf-8')
    assert len(b) == 3
    b = bytearray('abc你好', 'utf-8')
    assert len(b) == 9

    # Copy from other objects
    b = bytearray([1, 2, 3, 4])
    c = bytearray(b)
    assert c == b
    assert id(c) != id(b)


def bytearray_properties():
    # length
    b = bytearray()
    assert len(b) == 0

    # type of bytearray
    assert type(b) == bytearray


def bytearray_operations():
    b = bytearray(b'hello world')

    # access element
    assert b[0] == 104
    assert b[-1] == 100

    # unpacking variables
    t1, t2, t3, t4, t5, t6, t7, t8, t9, t10, t11 = b
    assert t1 == 104
    assert t11 == 100

    # max, min value
    assert max(b) == ord('w')
    assert min(b) == ord(' ')

    # partial copy
    c = b[2:5]
    assert c == bytearray(b'llo')

    # conversion - to string
    s = b.decode('utf-8')
    assert s == 'hello world'

    # conversion - to list
    l1 = list(b)
    assert l1 == [ord('h'), ord('e'), ord('l'), ord('l'), ord('o'), ord(' '),
                  ord('w'), ord('o'), ord('r'), ord('l'), ord('d'), ]

    # iterator
    i = iter(b)
    t = i.__next__()
    assert t == ord('h')

    # loop
    for t in b:
        pass
    assert t == ord('d')

    # Loop in reverse order
    for t in reversed(b):
        pass
    assert t == ord('h')

    # find value exists
    assert b'l' in b

    # find index of first occurrence
    assert b.find(b'h') == 0

    # find index of last occurrence
    assert b.rfind(b'd') == 10

    # count occurrence
    assert b.count(b'l') == 3

    # change value
    b[0] = ord('H')
    assert b[0] == ord('H')

    # replace a slice
    print(b)
    b[6:11] = b'Peter'  # note: the upper bound is exclusive
    assert b == bytearray(b'Hello Peter')

    # sort to a list
    list1 = sorted(b)
    assert list1 == [32, 72, 80, 101, 101, 101, 108, 108, 111, 114, 116]


def bytearray_error_handling():
    b = bytearray(b'hello world')

    # IndexError
    handled = False
    try:
        print(b[100])
        assert False  # this will not be reached.
    except IndexError as e:
        handled = True
    assert handled is True


if __name__ == "__main__":
    bytearray_initialization()
    bytearray_properties()
    bytearray_operations()
    bytearray_error_handling()
