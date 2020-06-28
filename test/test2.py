import unittest

from src.code2 import expo as this_func


class Code2Test(unittest.TestCase):
    def test_expo_0_is_1(self):
        self.assertEqual(this_func(2, 0), 1)

    def test_n_expo_1_n_times_n(self):
        self.assertEqual(this_func(2, 1), 2)

    def test_n_expo_2_n_times_n(self):
        self.assertEqual(this_func(2, 2), 2 * 2)

    def test_n_expo_12(self):
        self.assertEqual(this_func(2, 12), 2 ** 12)


if __name__ == "__main__":
    unittest.main()
