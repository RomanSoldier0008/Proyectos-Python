import unittest
from Add import Add
from Subtraction import Subtraction
from Division import Division
from Multiplication import Multiplication
from Constants import RESULT, RESULT_EXTENSION

class Test(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(Add(2, 2).add_and_return(), RESULT.format(4) + RESULT_EXTENSION)

    def test_resta(self):
        self.assertEqual(Subtraction(2, 2).subtract_and_return(), RESULT.format(0) + RESULT_EXTENSION)

    def test_multiplicacion(self):
        self.assertEqual(Multiplication(2, 2).multiply_and_return(), RESULT.format(4) + RESULT_EXTENSION)

    def test_division(self):
        self.assertEqual(Division(2, 2).divide_and_return(), RESULT.format(1) + RESULT_EXTENSION)