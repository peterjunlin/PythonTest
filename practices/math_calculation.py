import math


def math_builtins():
    assert abs(-123) == 123
    assert abs(-123.456) == 123.456
    assert abs(2+3j) == math.sqrt(2**2 + 3**2)

    assert divmod(5, 2) == (2, 1)
    assert max(1, 2, 3, 4) == 4
    assert min(1, 2, 3, 4) == 1

    a = 2
    b = 3
    c = 7
    assert pow(a, b) == a ** b
    assert pow(a, b, c) == a ** b % c

    assert round(123.05) == 123
    assert round(123.65) == 124

    assert round(-123.05) == -123
    assert round(-123.65) == -124

    assert round(123.65, 1) == 123.7
    assert round(-123.65, 1) == -123.7

    lst = [1, 2, 3]
    assert sum(lst) == 6


def math_module_constants():
    assert math.pi == 3.141592653589793
    assert math.tau == 6.283185307179586
    assert math.e == 2.718281828459045

    x = float('NaN')
    assert math.isnan(x)

    x = float('inf')
    assert math.isinf(x)
    x = math.inf
    assert math.isinf(x)
    x = -math.inf
    assert math.isinf(x)


def math_module():
    x = -1.23
    assert math.fabs(x) == 1.23


if __name__ == "__main__":
    math_builtins()
    math_module_constants()
    math_module()
