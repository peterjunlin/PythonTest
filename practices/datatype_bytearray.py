def bytearray_1():
    # declare empty object
    b = bytearray()
    print('b = bytearray()', type(b))
    # declare bytearray with size
    b = bytearray(10)
    print('b = bytearray(10)', b)
    # declare source from string
    b = bytearray('abc', 'utf-8')
    print('bytearray(\'abc\', \'utf-8\')', b)
    # Copy from other objects
    b = bytearray([1, 2, 3, 4])
    print('b = bytearray([1, 2, 3, 4])', b)
    b = bytearray(b'abcdef')
    print("b = bytearray(b'abcdef')",b)
    c = b
    print("c = b", c)
    # Get length
    print('len(b)', len(b))
    # read
    print('first element b[0] = ', b[0], chr(b[0]))
    print('last element b[-1] = ', b[-1], chr(b[-1]))
    try:
        print(b[10])
    except IndexError as e:
        print('b[10] = ', e)
    # unpacking variables
    t1, t2, t3, t4, t5, t6 = b
    print('t1, t2, t3, t4, t5, t6 = b\n', t1, t2, t3, t4, t5, t6)
    # max value
    print('max(b)', max(b))
    print('min(b)', min(b))
    # partial copy
    c = b[1:5]
    print('c = b[1:5]', c)
    # conversion
    s = b.decode('utf-8')
    print("To string: s = b.decode('utf-8')", s)
    l1 = list(b)
    print("To list: l1 = list(b)", l1)
    # iterator
    i = iter(b)
    t = i.__next__()
    print('i.__next__()', t)
    # loop
    print('Loop in order')
    for t in b:
        print(t)
    print('Loop in reverse order')
    for t in reversed(b):
        print(t)
    # find value exists
    if b'a' in b:
        print('\'a\' in b')
    else:
        print('\'a\' not in b')
    # find index of first occurrence
    index1 = b.find(b'b')
    print("index1 = b.find(b'b')", index1)
    # find index of last occurrence
    index1 = b.rfind(b'b')
    print("index1 = b.rfind(b'b')", index1)
    # count occurrence
    print("b.count(b'b')", b.count(b'b'))
    # change value
    print(b)
    b[0] = 98
    print('b[0] = 98', b)
    b[-1] = 98
    print('b[-1] = 98', b)
    # sort to a list
    k = bytearray(b'cafdkl')
    print("k = bytearray(b'cafdkl')\n sorted(k) = ", sorted(k))
    # replace a slice
    k[0:2] = b'ab'
    print("k[0:2] = b'ab'", k)

def practice1():
    bytearray_1()
