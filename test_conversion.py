import unittest
from calculator import ConversionRate

class TestCalc(unittest.TestCase):
    def test_correct(self): 
        carcount = 100
        armwashes = 50
        planssold = 5
        result = ConversionRate(carcount, armwashes, planssold)
        self.assertEqual(result,10)

if __name__ == '__main__':
    unittest.main()