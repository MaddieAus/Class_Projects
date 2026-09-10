"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment class 25
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from main25 import OrthoSeg

class TestOrthoSeg(unittest.TestCase): # I make the names of the tests explain itself

    def test_basic_intersection(self):
        segments = [
            ("H", 1, 5, 3),
            ("H", 2, 6, 5),
            ("V", 4, 2, 6)
        ]
        result = OrthoSeg(segments)
        expected = [(4, 3), (4, 5)]
        self.assertEqual(set(result), set(expected)) # i dont really care about order just that all the correct intersection points are there...

    def test_no_intersection(self):
        segments = [
            ("H", 1, 3, 1),
            ("V", 5, 2, 4)
        ]
        result = OrthoSeg(segments)
        self.assertEqual(result, [])

    def test_single_intersection(self):
        segments = [
            ("H", 0, 10, 4),
            ("V", 5, 0, 5)
        ]
        result = OrthoSeg(segments)
        expected = [(5, 4)]
        self.assertEqual(result, expected)

    def test_multiple_verticals(self):
        segments = [
            ("H", 1, 10, 2),
            ("H", 1, 10, 4),
            ("V", 3, 1, 5),
            ("V", 7, 1, 5)
        ]
        result = OrthoSeg(segments)
        expected = [(3, 2), (3, 4), (7, 2), (7, 4)]
        self.assertEqual(set(result), set(expected))


if __name__ == "__main__":
    unittest.main()