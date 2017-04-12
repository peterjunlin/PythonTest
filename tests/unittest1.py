import unittest
import practices.json1


class TestCase1(unittest.TestCase):
    def setUp(self):
        print('\nsetup1\n')

    def tearDown(self):
        print('\ntearDown1\n')

    def test1(self):
        list1 = [1, 2, 3]
        s1 = practices.json1.get_json_string(list1)
        print("test1")
        self.assertTrue(s1 == "[1, 2, 3]")


class TestCase2(unittest.TestCase):
    def setUp(self):
        print('\nsetup2\n')

    def tearDown(self):
        print('\ntearDown2\n')

    def test2(self):
        self.assertEqual(1, 1)
        print('\ntest2\n')


def main():
    unittest.main()


if __name__ == '__main__':
    main()
