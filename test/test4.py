import unittest

from src.code4 import sum_integer_loop as this_func_loop
from src.code4 import sum_integer_recursion as this_func_recursion

# Python has the `sum` function with takes an interable as an argument
# and returns the sum of the elements in the iterable


class Code4TestLoop(unittest.TestCase):

    def test_loop_between_0_1000(self):
        self.assertEqual(this_func_loop(0, 1000), sum(range(0, 1001)))

    def test_loop_betweem_neg_1000_to_pos_1000000(self):
        self.assertEqual(this_func_loop(-1000, 1000000),
                         sum(range(-1000, 1000000 + 1)))


class Code4TestRecursion(unittest.TestCase):

    def test_recursion_between_0_900(self):
        self.assertEqual(this_func_recursion(0, 900), sum(range(0, 900 + 1)))

    def test_recursion_betweem_neg_1_to_pos_900(self):
        self.assertEqual(this_func_recursion(-1, 900),
                         sum(range(-1, 900 + 1)))


class Code4TestLoopVsRecursion(unittest.TestCase):

    def test_loop_vs_recursion_between_0_900(self):
        self.assertEqual(this_func_loop(0, 900), this_func_recursion(0, 900))

    def test_loop_vs_recursion_betweem_neg_1_to_pos_900(self):
        self.assertEqual(this_func_loop(-1, 900),
                         this_func_recursion(-1, 900))


if __name__ == "__main__":
    unittest.main()
