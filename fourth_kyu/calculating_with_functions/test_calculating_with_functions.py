import unittest
from calculating_with_functions import *

class TestCalc(unittest.TestCase):

    def test_plus(self):
        self.assertEqual(one(plus(two())), three())
        self.assertEqual(three(plus(two())), five())
        self.assertEqual(zero(plus(five())), five())
        self.assertEqual(five(plus(five())), 10)
        self.assertEqual(six(plus(nine())), 15)

    def test_minus(self):
        self.assertEqual(three(minus(two())), one())
        self.assertEqual(five(minus(five())), zero())
        self.assertEqual(one(minus(two())), -1)
        self.assertEqual(zero(minus(five())), -5)
        self.assertEqual(six(minus(nine())), -3)

    def test_times(self):
        self.assertEqual(three(times(two())), six())
        self.assertEqual(one(times(two())), two())
        self.assertEqual(zero(times(five())), zero())
        self.assertEqual(five(times(five())), 25)
        self.assertEqual(six(times(nine())), 54)

    def test_divided_by(self):
        self.assertEqual(three(divided_by(two())), one())
        self.assertEqual(one(divided_by(two())), zero())
        self.assertEqual(zero(divided_by(five())), zero())
        self.assertEqual(five(divided_by(five())), one())
        self.assertEqual(six(divided_by(nine())), zero())

if __name__ == '__main__':
    unittest.main()