#calculator test
# import unittest
from unittest import TestCase
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        a = 10; b = 2; r = a + b
        self.assertEqual(self.calc.add(a,b), r)

    def test_subtraction(self):
        a = 10; b = 2; r = a - b
        self.assertEqual(self.calc.subtract(a, b), r)
    
    def test_multiplication(self):
        a = 10; b = 2; r = a * b
        self.assertEqual(self.calc.multiply(a,b), r)
    
    def test_division(self):
        a = 10; b = 2; c = 0; r = a / b
        self.assertIsNone(self.calc.divide(a, c))
        self.assertEqual(self.calc.divide(a, b), r)

