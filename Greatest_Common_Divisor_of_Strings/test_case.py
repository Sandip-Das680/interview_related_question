import unittest
from Solution import solution

class TestGcdOfStrings(unittest.TestCase):

    def setUp(self):
        self.obj = solution()

    def test_example1(self):
        self.assertEqual(self.obj.gcd_of_string("ABCABC", "ABC"), "ABC")

    def test_example2(self):
        self.assertEqual(self.obj.gcd_of_string("ABABAB", "ABAB"), "AB")

    def test_example3(self):
        self.assertEqual(self.obj.gcd_of_string("LEET", "CODE"), "")

    def test_example4(self):
        self.assertEqual(self.obj.gcd_of_string("AAAAAB", "AAA"), "")

    def test_same_strings(self):
        self.assertEqual(self.obj.gcd_of_string("AAAA", "AAAA"), "A")

    def test_one_char_repeat(self):
        self.assertEqual(self.obj.gcd_of_string("AAAAAA", "AA"), "AA")

    def test_no_common_pattern(self):
        self.assertEqual(self.obj.gcd_of_string("ABCDEF", "ABC"), "")

    def test_large_input(self):
        self.assertEqual(self.obj.gcd_of_string("XY" * 100, "XY" * 50), "XY")

    def test_single_character(self):
        self.assertEqual(self.obj.gcd_of_string("A", "A"), "A")

if __name__ == "__main__":
    unittest.main()
