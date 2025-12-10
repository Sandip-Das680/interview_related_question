import unittest

from code import solution

class TestMergeAlternately(unittest.TestCase):

    def setUp(self):
        self.sol= solution()

    def test_example_1(self):
        word1 = "abc"
        word2 = "pqr"
        expected = "apbqcr"
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

    def test_example_8(self):
        word1= "pd"
        word2= "wrt"
        expected= "pwdrt"
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

    def test_example_2(self):
        word1 = "ab"
        word2 = "pqrs"
        expected = "apbqrs"
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

    def test_example_3(self):
        word1 = "abcd"
        word2 = "pq"
        expected = "apbqcd"
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

    def test_empty_word1(self):
        word1 = ""
        word2 = "xyz"
        expected = "xyz"
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

    def test_empty_word2(self):
        word1 = "hello"
        word2 = ""
        expected = "hello"
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

    def test_both_empty(self):
        word1 = ""
        word2 = ""
        expected = ""
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

    def test_same_length(self):
        word1 = "aaa"
        word2 = "bbb"
        expected = "ababab"
        self.assertEqual(self.sol.merge_string(word1, word2), expected)

if __name__=='__main__':
    unittest.main


    

        