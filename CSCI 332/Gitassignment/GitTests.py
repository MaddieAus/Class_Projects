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
from GitMain import get_orientation#, do_intersect

class TestOrientation(unittest.TestCase):

    def test_collinear(self):
        self.assertEqual(
            get_orientation((0, 0), (2, 2), (4, 4)),
            0
        )

    def test_clockwise(self):
        self.assertEqual(
            get_orientation((0, 0),(1, 2), (4, 4)),
            1
        )

    def test_counterclockwise(self):
        self.assertEqual(
            get_orientation((0, 0), (4, 4), (2, 5)),
            2
        )

# def test_segments_intersect(self):
#     seg1 = ((1,1),(4,4))
#     seg2 = ((2,4),(4,2))
#     self.assertTrue(do_intersect(seg1, seg2))


# def test_segments_do_not_intersect(self):
#     seg1 = ((1,1),(2,2))
#     seg2 = ((3,3),(4,4))
#     self.assertFalse(do_intersect(seg1, seg2))
if __name__ == "__main__":
    unittest.main()