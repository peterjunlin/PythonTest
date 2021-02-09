def function_lambda(n):
    return lambda x: x + n


if __name__ == '__main__':
    pw = function_lambda(2)
    assert pw(3) == 5
