import struct


def struct_pack_and_unpack():
    # pack
    buffer = struct.pack('hhl', 1, 2, 3)  # short, short, long
    assert buffer == b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'

    # unpack
    a, b, c = struct.unpack('hhl', buffer)
    assert (a, b, c) == (1, 2, 3)


if __name__ == '__main__':
    struct_pack_and_unpack()
