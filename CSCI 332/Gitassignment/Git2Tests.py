"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 16 tests.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from Git2Main import convex_hull_jarvis


class TestConvexHull(unittest.TestCase):

    def test_square(self):
        points = [
            (0,0),
            (0,1),
            (1,1),
            (1,0)
        ]

        hull = convex_hull_jarvis(points)

        expected = [
            (0,0),
            (1,0),
            (1,1),
            (0,1)
        ]

        self.assertEqual(set(hull), set(expected)) # doesn't really matter the order just that the points are the same

    def test_triangle(self):
        points = [
            (0,0),
            (2,0),
            (1,2)
        ]

        hull = convex_hull_jarvis(points)

        self.assertEqual(set(hull), set(points))

    def test_complex_shape(self):
        points = [
            (0,3),
            (2,2),
            (1,1),
            (2,1),
            (3,0),
            (0,0),
            (3,3)
        ]

        hull = convex_hull_jarvis(points)

        expected = [
            (0,0),
            (3,0),
            (3,3),
            (0,3)
        ]

        self.assertEqual(set(hull), set(expected))


if __name__ == "__main__":
    unittest.main()