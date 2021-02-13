"""In terminal, run 'pytest -s QC_pytest_multi_functions.py -v'"""
import pytest
from random import randint

# k, v

# functions and dataset


def func1(data_item):
    print('func1', data_item)


def func2(data_item):
    print('func2', data_item)


def func3(data_item):
    print('func3', data_item)


function_list = [func1, func2, func3]


def generate_list():
    num_length = randint(0, 10)
    return [randint(0, 100) for _ in range(num_length)]


def generate_dataset():
    """dataset = [[...], ..., [...]]"""
    num_list = 10
    return [generate_list() for _ in range(num_list)]


@pytest.mark.parametrize("func", function_list)  # inner loop
@pytest.mark.parametrize("data_item1", generate_dataset())  # outer loop
def test_func(func, data_item1):
    func(data_item1)
