"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 07 (i think) OOP main.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from matchers import BruteForceMatcher, KMPMatcher, BoyerMooreMatcher


class TestStringMatchers(unittest.TestCase):

    def setUp(self):
        self.matchers = [
            BruteForceMatcher(),
            KMPMatcher(),
            BoyerMooreMatcher()
        ]

    def test_standard_match(self):
        for matcher in self.matchers:
            self.assertEqual(
                matcher.find_matches("abababab", "abab"),
                [0, 2, 4]
            )

    def test_no_match(self):
        for matcher in self.matchers:
            self.assertEqual(
                matcher.find_matches("hello world", "xyz"),
                []
            )

    def test_empty_pattern(self):
        for matcher in self.matchers:
            self.assertEqual(
                matcher.find_matches("hello", ""),
                []
            )

    def test_empty_text(self):
        for matcher in self.matchers:
            self.assertEqual(
                matcher.find_matches("", "hi"),
                []
            )

    def test_pattern_longer_than_text(self):
        for matcher in self.matchers:
            self.assertEqual(
                matcher.find_matches("hi", "hello"),
                []
            )


if __name__ == "__main__":
    unittest.main()