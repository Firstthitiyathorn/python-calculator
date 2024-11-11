import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    
    def test_add(self):
        self.assertEqual(self.calc.add(-1, -6), -7)
    def test_add(self):
        self.assertEqual(self.calc.add(4, 2), 6)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(-1, -2), 1)
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10, 15), -5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 3), 12)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(40, 2), 20)
    def test_divide(self):
        self.assertEqual(self.calc.divide(-30, 2), -15)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(30, 7), 2)
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(8, 3), 2)

if __name__ == '__main__':
    unittest.main()