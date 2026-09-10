"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class tests12.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""
import unittest
from main12 import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_basic_case(self):
        string1 = "ABCDGH"
        string2 = "AEDFHR"
        length, sequence = longest_common_subsequence(string1, string2)

        self.assertEqual(length, 3)
        self.assertEqual(sequence, "ADH")

    def test_empty_string(self):
        length, sequence = longest_common_subsequence("", "ABC")
        self.assertEqual(length, 0)
        self.assertEqual(sequence, "")

    def test_identical_strings(self):
        length, sequence = longest_common_subsequence("HELLO", "HELLO")
        self.assertEqual(length, 5)
        self.assertEqual(sequence, "HELLO")

    def test_no_common_subsequence(self):
        length, sequence = longest_common_subsequence("ABC", "DEF")
        self.assertEqual(length, 0)
        self.assertEqual(sequence, "")


if __name__ == "__main__":
    unittest.main()