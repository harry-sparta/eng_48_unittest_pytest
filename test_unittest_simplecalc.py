import unittest
from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    Calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.Calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.Calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.Calc.multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(self.Calc.divide(8, 4), 2)

