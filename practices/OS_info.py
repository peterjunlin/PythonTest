import sys


def byteorder():
    assert sys.byteorder == "little"


if __name__ == "__main__":
    byteorder()
