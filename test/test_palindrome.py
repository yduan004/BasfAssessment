import unittest
import sys
sys.path.append('../')
from src.palindrome import Palindrome

class TestPalindrome(unittest.TestCase):

    def test_find_anagrams(self):
        obj = Palindrome('art mom eat dad civic')
        expected = ['mom', 'dad', 'civic']
        actual =obj.find_palindromes()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()