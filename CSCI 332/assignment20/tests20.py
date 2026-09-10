"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment class 20
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from main20 import graham_scan

class TestGrahamScan(unittest.TestCase):
    def test_basic_square(self):
        #Test a simple square with a point in the middle.
        points = [(0, 0), (2, 0), (2, 2), (0, 2), (1, 1)]
        # The hull should be the four corners, (1,1) is inside.
        expected = [(0, 0), (2, 0), (2, 2), (0, 2)]
        result = graham_scan(points)
        self.assertEqual(result, expected)

    def test_triangle(self):
        #Test a simple triangle.
        points = [(0, 0), (5, 0), (2, 5)]
        result = graham_scan(points)
        self.assertEqual(result, [(0, 0), (5, 0), (2, 5)])

    def test_collinear_points(self):
        #Test how the algorithm handles points on the same line.
        points = [(0, 0), (1, 0), (2, 0), (1, 1)]
        # Based on your orientation check (<= 0), it should pop the middle collinear point (1,0).
        result = graham_scan(points)
        self.assertEqual(result, [(0, 0), (2, 0), (1, 1)])

    def test_minimum_points(self):
        #Test with only 3 points (the minimum for a 2D hull).
        points = [(0, 0), (1, 1), (0, 1)]
        result = graham_scan(points)
        self.assertEqual(len(result), 3)

if __name__ == '__main__':
    unittest.main()