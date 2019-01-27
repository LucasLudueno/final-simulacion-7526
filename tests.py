#!/usr/bin/python
from PageRank import PageRank
import numpy as np
import unittest

class TestPageRankClass(unittest.TestCase):
		
    def test_build_matrix_function(self):
        pageRank = PageRank()

        page_graph = np.matrix([[0, 1, 1], [0, 0, 1], [1, 0, 0]])
        expected_matrix = np.matrix([[ 0.05, 0.475, 0.475], [0.05, 0.05, 0.9], [0.9, 0.05, 0.05]])

        result_matrix = pageRank.build_matrix(page_graph)
        self.assertTrue(np.allclose(expected_matrix, result_matrix))

    def test_calculate_page_rank_function(self):
        pageRank = PageRank()

        page_graph = np.matrix([[0, 1, 1], [1, 0, 1], [1, 0, 0]])
        matrix = pageRank.build_matrix(page_graph)
        stacionary_state = [0.432748,  0.233918,  0.333333]

        page_rank_value = pageRank.calculate_page_rank(matrix)
        self.assertTrue(np.allclose(stacionary_state, page_rank_value))

if __name__ == '__main__':
    unittest.main()
