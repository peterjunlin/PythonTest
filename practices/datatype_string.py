"""Note: string is immutable."""

import sys


def string_literal():
    s = b'abc'  # ASCII
    s = u'abc'  # UTF

    s = r'abc\n'  # raw
    assert s == 'abc\\n'

    s = rb'abc'
    # s = ru'abc'  # this is not supported

    # Concatenation
    s = 'abc' 'def'
    assert s == 'abcdef'


def string_escape():
    s = 'abc\n'
    s = 'abc\'def\''


def string_literal_sharing():
    s = "abcdefg"
    b = s
    c = "abcdefg"
    d = "abcde"
    d = d + "fg"

    assert id(b) == id(s)  # string literal is shared, since the content is the same.
    assert id(c) == id(s)  # string literal is shared, since the content is the same.

    assert d == s
    assert id(d) != id(s)  # the calculated value is not treated as constant value.

    assert id(s[1:3]) == id(s[1:4])  # slice is a reference

    s1 = s[1:3]  # copy assignment
    s2 = s[1:4]  # copy assignment
    assert id(s1) != id(s2)


def string_functions():
    s1 = '  abc '
    s2 = 'hello'

    # Remove white space at the both ends.
    assert s1.strip() == "abc"

    # Capitalize first letter.
    assert s2.capitalize() == "Hello"

    # Find index of first occurrence
    assert s1.find('a') == 2

    # reverse
    s3 = ''.join(reversed(s2))
    assert s3 == "olleh"
    s3 = s2[::-1]
    assert s3 == "olleh"

    # Iteration
    it = reversed(s2)
    s4 = ''
    for i in it:
        s4 = s4 + i
    assert s4 == "olleh"

    # Concatenation
    sep = '/'
    d = ['2020', '1', '1']
    k = sep.join(d)
    assert k == '2020/1/1'


if __name__ == "__main__":
    string_literal()
    string_escape()
    string_literal_sharing()
    string_functions()
