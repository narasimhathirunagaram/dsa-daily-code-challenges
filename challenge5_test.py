import unittest
from challenge5 import product_array_except_self
class MyTestCase(unittest.TestCase):
    
    def check_case(self, nums, expected):
        self.assertEqual(product_array_except_self(nums),expected)
    def test_data1(self):
        self.check_case([1,2,3,4],[24,12,8,6])
    def test_data2(self):
        self.check_case([-1,1,0,-3,3],[0,0,9,0,0])

if __name__=='__main__':
    unittest.main()