""" Using fixture to do setup and tear down.
In terminal, run 'pytest -s QC_pytest_setup_teardown.py -v'"""

import pytest
from random import randint


def func1(data1):
    print('func1', data1)
    return sum(data1)


def func2(data1):
    print('func2', data1)
    return max(data1)


@ pytest.fixture
def setup():
    # setup
    print("\nsetup")

    yield

    # teardown
    print("\nteardown")


def generate_dataset():
    num_length = 4
    lst = [randint(0, 10) for _ in range(0, num_length)]
    return [lst for _ in range(0, num_length)]


@pytest.mark.parametrize("d1", generate_dataset())
def test_func1(setup, d1):
    assert func1(d1) == sum(d1)


@pytest.mark.parametrize("d1", generate_dataset())
def test_func2(setup, d1):
    assert func2(d1) == max(d1)
