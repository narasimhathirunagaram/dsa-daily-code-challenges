from challenge6 import longest_substring
import unittest

class MyTestCase(unittest.TestCase):
    def check_case(self,input,expected):
        self.assertEqual(longest_substring(input),expected)
    def test_sample1(self):
        self.check_case("abcabcbb",3)
    def test_sample2(self):
        self.check_case("bbbbb",1)
    def test_sample3(self):
        self.check_case("pwwkew",3)

if __name__=='__main__':
    unittest.main()