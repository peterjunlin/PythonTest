import unittest


class TestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    def setUp(self):
        print('setUp')

    def test_asert(self):
        # self.assertTrue(True == False)
        # self.assertTrue(False)
        print('testcase1')

    def test_2(self):
        self.assertEqual(1,1)
        print('\ntest2\n')

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")


class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass2")

    def setUp(self):
        print('setUp2')

    def test_asert(self):
        # self.assertTrue(True == False)
        # self.assertTrue(False)
        print('testcase2')

    def test_22(self):
        self.assertEqual(1,1)
        print('\ntest22\n')

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass2")


if __name__ == '__main__':
    unittest.main()
