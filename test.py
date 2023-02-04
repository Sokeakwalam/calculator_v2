import unittest
from calculator import Calculate as C

class TestCalculator(unittest.TestCase):
    def test_bracket(self):
        data = "(2+1*5)"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 7.0)

    def test_off(self):
        data = "2(3*4)"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 24.0)
    
    def test_power(self):
        data = "2^2"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 4.0)

    def test_multiplicataion(self):
        data = "2*3*4"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 24.0)

    def test_division(self):
        data = "8/2"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 4.0)

    def test_sum(self):
        data = "2+3"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 5.0)

    def test_subtraction(self):
        data = "10-5"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 5.0)
    
    def test_double_minus(self):
        data = "10--5"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 15.0)

    def test_double_plus(self):
        data = "10++5"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 15.0)

    def test_minus_plus(self):
        data = "10-+5"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 5.0)

    def test_plus_minus(self):
        data = "10-+5"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 5.0)

    def test_combination(self):
        data = "2*2(4)+(5-2)-8/2^2"
        calculator = C(data)
        source = calculator.calculations()
        self.assertEqual(source, 17.0)

    def test_zero_division_error(self):
        data = "2/0"
        calculator = C(data)
        with self.assertRaises(ZeroDivisionError):
            calculator.calculations()
    
    def test_value_error(self):
        data = "2/p"
        calculator = C(data)
        with self.assertRaises(ValueError):
            calculator.calculations()
    

            
            


    





if __name__ == '__main__':
    unittest.main()