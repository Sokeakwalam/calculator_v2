import unittest
from calculator import Calculate as C



class TestCalculator(unittest.TestCase):
    def test_bracket(self):
        data = "(2+1*5)"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 7)

    def test_off(self):
        data = "2(3*4)"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 24)
    
    def test_power(self):
        data = "2^2"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 4)

    def test_multiplicataion(self):
        data = "2*3*4"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 24)

    def test_division(self):
        data = "8/2"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 4)

    def test_sum(self):
        data = "2+3"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 5)

    def test_subtraction(self):
        data = "10-5"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 5)
    
    def test_double_minus(self):
        data = "10--5"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 15)

    def test_double_plus(self):
        data = "10++5"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 15)

    def test_minus_plus(self):
        data = "10-+5"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 5)

    def test_plus_minus(self):
        data = "10-+5"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 5)

    def test_combination(self):
        data = "2*2(4)+(5-2)-8/2^2"
        calculator = C(data)
        result = calculator.calculations()
        self.assertEqual(result, 17)

    def test_zero_division_error(self):
        data = 2/0
        calculator = C(data)
        result = calculator.calculations()
        self.assertRaises(ZeroDivisionError, result)


    





if __name__ == '__main__':
    unittest.main()