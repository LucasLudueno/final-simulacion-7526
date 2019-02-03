#!/usr/bin/python
import sys
import numpy as np
import unittest

sys.path.append('../')
from PageRank import PageRank

class TestPageRankClass(unittest.TestCase):
		
    def test_build_matrix_function_for_3_nodes(self):
        pageRank = PageRank()

        page_graph = np.matrix([[0, 1, 1], [0, 0, 1], [1, 0, 0]])
        expected_matrix = np.matrix([[ 0.05, 0.475, 0.475], [0.05, 0.05, 0.9], [0.9, 0.05, 0.05]])

        result_matrix = pageRank.build_matrix(page_graph)
        self.assertTrue(np.allclose(expected_matrix, result_matrix))

    def test_build_matrix_function_for_4_nodes(self):
        pageRank = PageRank()

        page_graph = np.matrix([[0, 1, 1, 0], [0, 0, 1, 1], [1, 0, 0, 0], [0, 0, 0 ,0]])
        expected_matrix = np.matrix([[0.0375, 0.4625, 0.4625, 0.0375], [0.0375, 0.0375, 0.4625, 0.4625], [0.8875, 0.0375, 0.0375, 0.0375], [0.25, 0.25, 0.25, 0.25]])

        result_matrix = pageRank.build_matrix(page_graph)
        self.assertTrue(np.allclose(expected_matrix, result_matrix))

    def test_calculate_page_rank_function_3_nodes(self):
        pageRank = PageRank()

        page_graph = np.matrix([[0, 1, 1], [1, 0, 1], [1, 0, 0]])
        matrix = pageRank.build_matrix(page_graph)
        stacionary_state = [0.432748,  0.233918,  0.333333]

        page_rank_value = pageRank.calculate_page_rank(matrix)
        self.assertTrue(np.allclose(stacionary_state, page_rank_value))

if __name__ == '__main__':
    unittest.main()

# TODO: GRAFO DE REFERENCIAS????
# TODO: GRAN MATRIZ Y CHEQUEAR QUE LA SUMA DEL PAGERANK ES 1
# TODO: debug mode
# TODO: BUSCAR SOLO POR PALABRAS 