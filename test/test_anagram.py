import unittest
import sys
sys.path.append('../')
from src.anagram import Anagram

class TestAnagram(unittest.TestCase):

    def test_find_anagrams(self):
        obj = Anagram('art')
        expected = ['art', 'atr', 'rat', 'rta', 'tar', 'tra']
        actual = obj.find_anagrams()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()