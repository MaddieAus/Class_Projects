"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class (structured python project) tests.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.

this is the tests of the main file
"""

## this is the test code to brute_force_match assignment ###

# import unittest

# from main import brute_force_match

# class TestBruteForceMatch(unittest.TestCase):

#     def test_normal_match(self): # all the names explain what the test is for. for exsample this is just a normal test
#         self.assertEqual(brute_force_match("Mississippi", "iss"), [1, 4])

#     def test_overlapping_matches(self): # this is if it overlaps
#         self.assertEqual(brute_force_match("aaaaa", "aa"), [0, 1, 2, 3])

#     def test_single_match(self): # a single match
#         self.assertEqual(brute_force_match("hello", "ll"), [2])

#     def test_no_match(self): # no match
#         self.assertEqual(brute_force_match("hello", "world"), [])

#     def test_empty_text(self): # no text 
#         self.assertEqual(brute_force_match("", "a"), [])

#     def test_empty_pattern(self): # no pattern
#         self.assertEqual(brute_force_match("abc", ""), [0, 1, 2, 3])

# if __name__ == "__main__":
#     unittest.main()

### this is the test code for boyer_moore_match assignment ###

# import unittest
# from main import boyer_moore_match


# class TestBoyerMoore(unittest.TestCase):

#     def test_basic_match(self): # normal tests
#         self.assertEqual(boyer_moore_match("ABAAABCD", "ABC"), [4])

#     def test_multiple_matches(self): # more then one match
#         self.assertEqual(boyer_moore_match("AAAAA", "AA"), [0, 1, 2, 3])

#     def test_no_match(self): # no match found
#         self.assertEqual(boyer_moore_match("HELLO", "WORLD"), [])

#     def test_pattern_equals_text(self): # the same
#         self.assertEqual(boyer_moore_match("MATCH", "MATCH"), [0])

#     def test_single_character_pattern(self): # only one character
#         self.assertEqual(boyer_moore_match("BANANA", "A"), [1, 3, 5])

#     def test_repeated_pattern(self): # if repeated
#         self.assertEqual(boyer_moore_match("ABCABCABC", "ABC"), [0, 3, 6])

#     def test_empty_cases(self): # if empty
#         self.assertEqual(boyer_moore_match("", "A"), [])
#         self.assertEqual(boyer_moore_match("A", ""), [])
#         self.assertEqual(boyer_moore_match("", ""), [])


# if __name__ == "__main__":
#     unittest.main()

### tests for Knuth-Moriss-Pratt algorithm assignment ###

# import unittest
# from main import knuth_morris_pratt_match

# class TestKMP(unittest.TestCase):

#     def test_basic_match(self): #normal test
#         text = "abracadabra"
#         pattern = "abra"
#         self.assertEqual(knuth_morris_pratt_match(text, pattern), [0, 7])

#     def test_single_match(self): #one match
#         text = "hello world"
#         pattern = "world"
#         self.assertEqual(knuth_morris_pratt_match(text, pattern), [6])

#     def test_no_match(self): #no matches
#         text = "abcdef"
#         pattern = "xyz"
#         self.assertEqual(knuth_morris_pratt_match(text, pattern), [])

#     def test_empty_pattern(self): # empty pattern
#         text = "abc"
#         pattern = ""
#         self.assertEqual(knuth_morris_pratt_match(text, pattern), [])

#     def test_empty_text(self): # empty text
#         text = ""
#         pattern = "abc"
#         self.assertEqual(knuth_morris_pratt_match(text, pattern), [])


# if __name__ == "__main__":
#     unittest.main()

### tests for knapsack algorithm assignment ###

import unittest
from main import fractional_knapsack

class TestFractionalKnapsack(unittest.TestCase):

    def test_standard_case(self):
        # Classic example
        items = [(60, 10), (100, 20), (120, 30)]
        capacity = 50.0
        total_value, fractions = fractional_knapsack(items, capacity)

        self.assertAlmostEqual(total_value, 240.0)
        self.assertEqual(len(fractions), 3)

    def test_exact_fit(self):
        # Capacity exactly matches item weights
        items = [(50, 10), (60, 20)]
        capacity = 30.0
        total_value, fractions = fractional_knapsack(items, capacity)

        self.assertAlmostEqual(total_value, 110.0)
        self.assertEqual(fractions, [(0, 1.0), (1, 1.0)])

    def test_fractional_item(self):
        # Only part of an item can be taken
        items = [(100, 20)]
        capacity = 10.0
        total_value, fractions = fractional_knapsack(items, capacity)

        self.assertAlmostEqual(total_value, 50.0)
        self.assertEqual(fractions, [(0, 0.5)])

    def test_zero_capacity(self):
        items = [(50, 10), (60, 20)]
        capacity = 0
        total_value, fractions = fractional_knapsack(items, capacity)

        self.assertEqual(total_value, 0.0)
        self.assertEqual(fractions, [])

    def test_empty_items(self):
        items = []
        capacity = 50
        total_value, fractions = fractional_knapsack(items, capacity)

if __name__ == "__main__":
    unittest.main()