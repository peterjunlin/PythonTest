import sys


def optional_list_arguments(a, lst=[]):
    # Mutable optional default value is initialized once and shared globally.
    lst.append(a)
    return lst


def optional_int_arguments(a, b=10):
    # Immutable optional default value is initialized once and shared in global scope as well.
    b += a
    return b


def function_positional_arguments_and_keyword_arguments(f, *p, **kw):
    assert type(p) == tuple
    assert p == (11, 12, 13, 14)

    assert type(kw) == dict
    assert kw == {'g': 15, 'h': 16}


if __name__ == '__main__':
    lst1 = optional_list_arguments(1)
    assert lst1 == [1]
    lst1 = optional_list_arguments(2)
    assert lst1 == [1, 2]

    k = optional_int_arguments(1)
    assert k == 11
    k = optional_int_arguments(1)
    assert k == 11

    function_positional_arguments_and_keyword_arguments(10, 11, 12, 13, 14, g=15, h=16)
