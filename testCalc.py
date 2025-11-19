import unittest

from calc import Calculator


class testCalc(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(4, 5), 9)
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
    def test_divide(self):
        self.assertEqual(self.calc.divide(3, 2), 1)
    def test_substract(self):
        self.assertEqual(self.calc.subtract(10, 5), 2)
    
if __name__ == "__main__":
    unittest.main()