import unittest
from calculator import ConversionRate

class TestCalc(unittest.TestCase):
    def correct(self): 
        carcount = 100
        armwashes = 50
        planssold = 5
        result = ConversionRate(carcount, armwashes, planssold)
        self.assertEqual(result,10)

    def incorrect(self):
        carcount = 100
        armwashes = 40
        planssold = 10
        result = ConversionRate(carcount, armwashes, planssold)
        self.assertEqual(result, 50)

if __name__ == '__main__':
    unittest.main()