import unittest

from src.code6 import (
    add_rat, denum_rat, div_rat,
    eq_rat, make_rat, mul_rat,
    num_rat, print_rat, sub_rat)


class Code6Test(unittest.TestCase):

    def setUp(self):
        self.half = [1, 2]
        self.third = [1, 3]

    def test_num_rat(self):
        self.assertEqual(num_rat(self.half), self.half[0])
        self.assertEqual(num_rat(self.third), self.third[0])

    def test_denum_rat(self):
        self.assertEqual(num_rat(self.half), self.half[0])
        self.assertEqual(num_rat(self.third), self.third[0])

    def test_make_rat(self):
        self.assertEqual(make_rat(self.half[0], self.half[1]), self.half)
        self.assertEqual(
            make_rat(self.half[0] * 2, self.half[1] * 2), self.half)

    def test_add_rat(self):
        self.assertEqual(add_rat(self.half, self.third), make_rat(5, 6))

    def test_sub_rat(self):
        self.assertEqual(sub_rat(self.half, self.third), make_rat(1, 6))

    def test_mul_rat(self):
        self.assertEqual(mul_rat(self.half, self.third), make_rat(1, 6))

    def test_div_rat(self):
        self.assertEqual(div_rat(self.half, self.third), make_rat(3, 2))

    def test_eq_rat(self):
        self.assertEqual(eq_rat(self.half, self.third), False)

    def test_print_rat(self):
        self.assertEqual(print_rat(self.half),  '1/2')
        self.assertEqual(print_rat(self.third), '1/3')
