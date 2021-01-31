import unittest


class TestBuiltin(unittest.TestCase):
    def test_abs(self):
        x = -0.1
        print(abs(x) == 0.1)

