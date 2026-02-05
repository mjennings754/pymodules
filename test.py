import unittest
from modules.arithmetic import *
from modules.reverse import *
from modules.fire import *
from modules.strings import *
from modules.magic import *
from modules.rcalc import *
from modules.smile import *
from modules.fact import *
from modules.cf import *
class TestArithmeticMethods(unittest.TestCase):
# ARITHMETIC MODULE
    def test_add(self):
        result = add(2, 3)
        assert result == 5

    def test_subtract(self):
        result = subtract(10, 5)
        assert result == 5

    def test_multiply(self):
        result = multiply(7, 7)
        assert result == 49

    def test_divide(self):
        result = divide(20, 5)
        assert result == 4

    def test_add_multiple(self):
        result = add_multiple(4, 5, 9)
        assert result == 18

    # CELSIUS TO FAHRENHEIT

    def test_convert_celsius_to_fahrenheit(self):
        assert convert_celsius_to_fahrenheit(10) == 50

if __name__ == '__main__':
    unittest.main()