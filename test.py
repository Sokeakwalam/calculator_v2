import unittest
from calculator import Calculate as C



class TestEquals(unittest.TestCase):
    
    data = "2*3+4/2(4)"
    calculator = C(data)
    result = calculator.calculations()
    answer = 32
    
    def test_sum(self):
        self.assertEqual(self.result, self.answer)

    def test_multiplicataion(self):
        self.assertEqual(self.result, self.answer)

    def test_division(self):
        self.assertEqual(self.result, self.answer)

    def test_bracket(self):
        self.assertEqual(self.result, self.answer)





if __name__ == '__main__':
    unittest.main()