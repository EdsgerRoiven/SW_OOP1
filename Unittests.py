import unittest
from main import *
class Unittest(unittest.TestCase):
    def test_method1(self):
        basic = Quicksort([ 4, 6, 8, 5, 1],0,4)
        result = [ 1, 4, 5, 6, 8 ]
        self.assertEqual(basic.ar,result)

    def test_method2(self):
        basic = Quicksort([1],0,0)
        result = [1]
        self.assertEqual(basic.ar, result)

    def test_method3(self):
        basic = Quicksort([1,2,3,4,5,6,7,8,9],0,8)
        result = [1,2,3,4,5,6,7,8,9]
        self.assertEqual(basic.ar, result)

    def test_method4(self):
        basic = Quicksort([48, 37, 86, 2, 7, 16, 30, 27, 33, 22, 18, 19, 87, 11, 1, 63, 14, 4, 20],0,18)
        result = [1, 2, 4, 7, 11, 14, 16, 18, 19, 20, 22, 27, 30, 33, 37, 48, 63, 86, 87]
        self.assertEqual(basic.ar, result)
if __name__ == '__main__':
    unittest.main(verbosity=2)