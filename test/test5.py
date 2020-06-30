import unittest

from src.code5 import f as this_func


class Code5Test(unittest.TestCase):

    def test_when_x_and_y_are_gt_or_eq_zero(self):
        x = 23
        y = 100
        self.assertEqual(this_func(x, y),
                         ((x * ((1 + (x * y))**2)) + (y * (1 - y)) + ((1 + (x * y)) * (1 - y))))

    def test_when_x_and_y_are_lt_zero(self):
        x = -23
        y = -100
        self.assertEqual(this_func(x, y),
                         ((x * ((1 + (x * y))**2)) + (y * (1 - y)) + ((1 + (x * y)) * (1 - y))))

    def test_when_x_and_y_are_gt_or_eq_1000(self):
        x = 1001
        y = 23000
        self.assertEqual(this_func(x, y),
                         ((x * ((1 + (x * y))**2)) + (y * (1 - y)) + ((1 + (x * y)) * (1 - y))))

    def test_when_x_and_y_are_lt_neg_1000(self):
        x, y = -1001, -2001
        self.assertEqual(this_func(x, y),
                         ((x * ((1 + (x * y))**2)) + (y * (1 - y)) + ((1 + (x * y)) * (1 - y))))


if __name__ == "__main__":
    unittest.main()
