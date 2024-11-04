import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3) 

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_subtract_one(self):
        self.assertEqual(self.calc.subtract(5, -2), 7)

    def test_subtract_two(self):
        self.assertEqual(self.calc.subtract(-5, 2), -7)
    
    def test_multiply_one(self):
        self.assertEqual(self.calc.multiply(6, 5), 30)
    
    def test_multiply_two(self):
        self.assertEqual(self.calc.multiply(-6, 5), -30)

    def test_divide_one(self):
        self.assertEqual(self.calc.divide(6, 3), 2)

    def test_divide_two(self):
        self.assertEqual(self.calc.divide(7, 2), 3)

    def test_modulo_one(self):
        self.assertEqual(self.calc.modulo(6, 2), 0)
    
    def test_modulo_two(self):
        self.assertEqual(self.calc.modulo(5, 0), "can not specify")
    

if __name__ == '__main__':
    unittest.main()