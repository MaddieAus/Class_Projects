"""
Madison Grace Austin
CSCI 332 Spring 2025
Programming Assignment # class27
I acknowledge that I have worked on this assignment independently, except where explicitly
noted and referenced. Any collaboration or use of external resources has been properly cited.
I am fully aware of the consequences of academic dishonesty and agree to abide by the
university's academic integrity policy. I understand the importance the consequences of
plagiarism.
"""
import unittest
from main27 import dijkstra

class TestDijkstra(unittest.TestCase):

    def test_normal_graph(self):
        graph = {
            "A": [("B", 4), ("C", 2)],
            "B": [("C", 1), ("D", 5)],
            "C": [("B", 3), ("D", 8), ("E", 10)],
            "D": [("E", 2)],
            "E": []
        }
        expected = {"A": 0, "B": 4, "C": 2, "D": 9, "E": 11}
        self.assertEqual(dijkstra(graph, "A"), expected)

    def test_single_node(self):
        graph = {"A": []}
        expected = {"A": 0}
        self.assertEqual(dijkstra(graph, "A"), expected)

    def test_disconnected_nodes(self):
        graph = {
            "A": [("B", 1)],
            "B": [],
            "C": [("D", 1)]
        }
        expected = {"A": 0, "B": 1}
        self.assertEqual(dijkstra(graph, "A"), expected)

    def test_empty_graph(self):
        graph = {}
        expected = {}
        self.assertEqual(dijkstra(graph, "A"), expected)

if __name__ == "__main__":
    unittest.main()