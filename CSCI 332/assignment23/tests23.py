"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment class 23
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from main23 import FindConvexHull

class TestConvexHull(unittest.TestCase):

    def test_basic_square(self):
        points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
        expected = [(0, 0), (2, 0), (2, 2), (0, 2)]
        result = FindConvexHull(points)
        self.assertEqual(set(result), set(expected))

    def test_triangle(self):
        points = [(0, 0), (5, 0), (2, 5)]
        result = FindConvexHull(points)
        self.assertEqual(set(result), set(points))

    def test_collinear_points(self):
        points = [(0, 0), (1, 0), (2, 0), (1, 1)]
        expected = [(0, 0), (2, 0), (1, 1)]
        result = FindConvexHull(points)
        self.assertEqual(set(result), set(expected))

    def test_minimum_points(self):
        points = [(0, 0), (1, 1), (0, 1)]
        result = FindConvexHull(points)
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()