import unittest

from src.code7 import makepoint, midpoint, printpoint, xpoint, ypoint


class Code7Test(unittest.TestCase):

    def setUp(self):
        self.pointA = [1, 2]
        self.pointB = [1, 3]

    def test_xpoint(self):
        self.assertEqual(xpoint(self.pointA), self.pointA[0])
        self.assertEqual(xpoint(self.pointB), self.pointB[0])

    def test_ypoint(self):
        self.assertEqual(ypoint(self.pointA), self.pointA[1])
        self.assertEqual(ypoint(self.pointB), self.pointB[1])

    def test_makepoint(self):
        self.assertEqual(makepoint(1, 2), self.pointA)
        self.assertEqual(makepoint(1, 3), self.pointB)

    def test_midpoint(self):
        self.assertEqual(midpoint(self.pointA, self.pointB), [1, 2])

    def test_printpoint(self):
        self.assertEqual(printpoint(self.pointA), '(1, 2)')
        self.assertEqual(printpoint(self.pointB), '(1, 3)')