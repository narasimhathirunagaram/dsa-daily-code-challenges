from challenge8 import Solution
import unittest

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        return super().setUp()

    def check_case(self,input,expected):
        nums, target = input
        self.assertEqual(self.sol.minSubArrayLen(target,nums),expected)
    
    def test_sample1(self):
        l1 = [[2,3,1,2,4,3], 7]
        self.check_case(l1,2)
    def test_sample2(self):
        l2 = [[1,4,4], 4]
        self.check_case(l2,1)
    def test_sample3(self):
        l3 = [[1,1,1,1,1,1,1,1], 11]
        self.check_case(l3,0)
    def test_sample4(self):
        l4 = [[12,28,83,4,25,26,25,2,25,25,25,12], 213]
        self.check_case(l4,8)

if __name__=='__main__':
    unittest.main()