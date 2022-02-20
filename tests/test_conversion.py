import unittest
from calculator import ConversionRate

class TestCalc(unittest.TestCase):
    def test_calc(self): 
        data = [100,50,5]
        result = ConversionRate(data)
        self.assertEqual(result,10)

if __name__ == '__main__':
    unittest.main()