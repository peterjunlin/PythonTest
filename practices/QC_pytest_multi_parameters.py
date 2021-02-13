"""In terminal, run 'pytest -s QC_pytest_multi_parameters.py -v'"""
import pytest
from random import randint


def func1(a, b, c):
    print('func1', a, b, c)


def generate_list():
    return [randint(0, 100), randint(0, 100), randint(0, 100)]


def generate_dataset():
    """dataset = [[a1, b1, c1], ..., [an, bn, cn]]"""
    num_list = 10
    return [generate_list() for _ in range(num_list)]


@pytest.mark.parametrize("a, b, c", generate_dataset())
def test_func(a, b, c):
    func1(a, b, c)
