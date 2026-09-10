"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class30
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""

import unittest
from main30 import connected_components

class TestConnectedComponents(unittest.TestCase):

    def test_fully_connected(self):
        graph = {
            "A": ["B"],
            "B": ["A", "C"],
            "C": ["B"]
        }
        result = connected_components(graph)
        self.assertEqual(len(result), 1)
        self.assertIn("A", result[0])
        self.assertIn("B", result[0])
        self.assertIn("C", result[0])

    def test_disconnected_graph(self):
        graph = {
            "A": ["B"],
            "B": ["A"],
            "C": ["D"],
            "D": ["C"]
        }
        result = connected_components(graph)
        self.assertEqual(len(result), 2)

    def test_single_node(self):
        graph = {"A": []}
        result = connected_components(graph)
        self.assertEqual(result, [["A"]])

    def test_empty_graph(self):
        graph = {}
        result = connected_components(graph)
        self.assertEqual(result, []) 

if __name__ == '__main__':
    unittest.main()