import unittest
from calculating_with_functions import *

class TestCalc(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(one(plus(two())), 3)
        self.assertEqual(three(plus(two())), 5)
        self.assertEqual(zero(plus(five())), 5)
        self.assertEqual(five(plus(five())), 10)
        self.assertEqual(six(plus(nine())), 15)

    def test_minus(self):
        self.assertEqual(three(minus(two())), 1)
        self.assertEqual(five(minus(five())), 0)
        self.assertEqual(one(minus(two())), -1)
        self.assertEqual(zero(minus(five())), -5)
        self.assertEqual(six(minus(nine())), -3)

    def test_times(self):
        self.assertEqual(three(times(two())), 6)
        self.assertEqual(one(times(two())), 2)
        self.assertEqual(zero(times(five())), 0)
        self.assertEqual(five(times(five())), 25)
        self.assertEqual(six(times(nine())), 54)

    def test_divided_by(self):
        self.assertEqual(three(divided_by(two())), 1)
        self.assertEqual(one(divided_by(two())), 0)
        self.assertEqual(zero(divided_by(five())), 0)
        self.assertEqual(five(divided_by(five())), 1)
        self.assertEqual(six(divided_by(nine())), 0)

if __name__ == '__main__':
    unittest.main()