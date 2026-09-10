"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class 08 main.py
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from main08 import greedy_scheduling

class TestTaskScheduling(unittest.TestCase):

    def test_single_task(self):
        tasks = [(0, 2, 10)]    # this is if the task is just one
        self.assertEqual(greedy_scheduling(tasks), 10)

    def test_no_overlap(self):
        tasks = [(1, 2, 5), (2, 3, 6), (3, 4, 7)]   # this is if there is no overlap
        self.assertEqual(greedy_scheduling(tasks), 18)

    def test_all_overlap(self):
        tasks = [(1, 5, 10), (2, 6, 20), (3, 7, 30)]    # if they all overlap
        self.assertEqual(greedy_scheduling(tasks), 10)

    def test_empty_list(self):
        tasks = []  # if you have a day off (no tasks)
        self.assertEqual(greedy_scheduling(tasks), 0)


if __name__ == "__main__":
    unittest.main()
