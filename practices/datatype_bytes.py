"""bytes is immutable"""


def bytes_initialization():
    # declare empty object
    b1 = bytes()
    assert len(b1) == 0

    # declare with size
    b2 = bytes(10)
    assert len(b2) == 10

    # initialized with generator
    b3 = bytes(range(10, 20, 2))
    assert len(b3) == 5

    b4 = b'hello world'
    assert type(b4) == bytes


def bytes_operations():
    b = bytes(range(0, 10, 1))

    # slice
    d = b[0:3]
    assert d == b'\x00\x01\x02'
    d = b[-3:]
    assert d == b'\x07\x08\x09'

    # assignment
    d = b
    assert id(d) == id(b)


def bytes_error_handling():
    b = bytes(range(0, 10, 2))
    handled = False
    try:
        a = b[10]
    except IndexError as e:
        handled = True
    assert handled


if __name__ == "__main__":
    bytes_initialization()
    bytes_operations()
    bytes_error_handling()
