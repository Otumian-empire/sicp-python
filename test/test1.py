import unittest

from src.code1 import f as this_func


class Code1Test(unittest.TestCase):

    def test_n_less_than_3(self):
        self.assertEqual(this_func(0), 0)
        self.assertEqual(this_func(1), 1)
        self.assertEqual(this_func(2), 2)

    def test_n_greater_than_3(self):
        self.assertNotEqual(this_func(3), 3)
        self.assertEqual(this_func(10), 1892)


if __name__ == "__main__":
    unittest.main()
