import unittest
from challenge7 import Solution

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
    
    def test_sample1(self):
        nums,k = [90],1
        self.assertEqual(self.sol.minimumDifference(nums,k),0)
    def test_sample2(self):
        nums,k = [9,4,1,7],2
        self.assertEqual(self.sol.minimumDifference(nums,k),1)

if __name__=='__main__':
    unittest.main()