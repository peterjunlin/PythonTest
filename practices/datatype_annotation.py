def annotation_of_function_return_value() -> int:
    return 10


def annotation_of_parameters(p: int, s: str):
    return "{0} {1}".format(p, s)


if __name__ == '__main__':
    k = annotation_of_function_return_value()
    assert k == 10
    s1 = annotation_of_parameters(10, 'apples')
    assert s1 == '10 apples'
