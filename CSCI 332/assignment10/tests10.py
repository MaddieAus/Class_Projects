"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 10 tests10.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from main10 import RodCutting


class TestRodCutting(unittest.TestCase):

    def test_example_case(self):
        n = 8
        prices = [1, 5, 8, 9, 10, 17, 17, 20]   # the test from the assignment
        revenue, cuts = RodCutting(n, prices)

        self.assertEqual(revenue, 22)
        self.assertEqual(sum(cuts), n)

    def test_single_length(self):
        n = 1
        prices = [3]
        revenue, cuts = RodCutting(n, prices)   # single length

        self.assertEqual(revenue, 3)
        self.assertEqual(cuts, [1])

    def test_no_cut_needed(self):
        n = 4
        prices = [1, 5, 8, 9]
        revenue, cuts = RodCutting(n, prices)   # no cut 

        self.assertEqual(revenue, 10)
        self.assertEqual(sum(cuts), n)

    def test_zero_length(self):
        revenue, cuts = RodCutting(0, [])   # nothing empty
        self.assertEqual(revenue, 0)
        self.assertEqual(cuts, [])


if __name__ == "__main__":
    unittest.main()
