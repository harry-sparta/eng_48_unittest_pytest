import unittest
from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):

    Calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.Calc.add(2, 4), 6)
        self.assertEqual(self.Calc.add(10, 17), 27)

    def test_subtract(self):
        self.assertEqual(self.Calc.subtract(4, 2), 2)
        self.assertEqual(self.Calc.subtract(99, 45), 54)

    def test_multiply(self):
        self.assertEqual(self.Calc.multiply(2, 3), 6)
        self.assertEqual(self.Calc.multiply(20, 11), 220)

    def test_divide(self):
        self.assertEqual(self.Calc.divide(8, 4), 2)
        self.assertEqual(self.Calc.divide(66, 3), 22)

