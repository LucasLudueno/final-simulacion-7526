#!/usr/bin/python
import sys
import numpy as np
import unittest

sys.path.append('../')
from PageRank import PageRank

class TestPageRankClass(unittest.TestCase):
	
    # For build matrix function
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

    # For page rank calculation
    def test_page_rank_properties_with_1000_nodes_by_matrix(self):
        file = open("../page_rank_files/epa_graph.txt", "r")
        file.readline()
        nodes = 1000
        page_graph = np.zeros([nodes, nodes], dtype=np.uint8)

        # Iterate edges in file and add them to the graph
        for edge in file:
            source = int(edge.split()[0])
            dest = int(edge.split()[1])
            if source < nodes and dest < nodes:
                page_graph[int(source)][int(dest)] = 1

        pageRank = PageRank()

        # check all rows have 1.0 as sum
        matrix = pageRank.build_matrix(page_graph)
        for row in matrix:
            values_sum = sum(row.A[0])

            for value in row.A[0]:
                self.assertTrue(0.0 < value)
                self.assertTrue(value < 1.00000000001)

            self.assertTrue(0.99999999999 < values_sum)
            self.assertTrue(values_sum < 1.00000000001)

        # check all page rank values sum is 1.0
        page_rank_values = pageRank.calculate_page_rank(matrix)
        for value in page_rank_values:
            self.assertTrue(0.0 < value)
            self.assertTrue(value < 1.00000000001)

        total_page_rank = sum(page_rank_values)
        self.assertTrue(0.99999999999 < total_page_rank)
        self.assertTrue(total_page_rank < 1.00000000001)

    def test_page_rank_properties_with_1000_nodes_by_matrix_and_eigen_matrix(self):
        file = open("../page_rank_files/notre_dam_graph.txt", "r")
        file.readline()
        nodes = 100
        page_graph = np.zeros([nodes, nodes])

        # Iterate edges in file and add them to the graph
        for edge in file:
            source = int(edge.split()[0])
            dest = int(edge.split()[1])
            if source < nodes and dest < nodes:
                page_graph[int(source)][int(dest)] = 1

        pageRank = PageRank()

        # check all rows have 1.0 as sum
        matrix = pageRank.build_matrix(page_graph)
        for row in matrix:
            values_sum = sum(row.A[0])

            for value in row.A[0]:
                self.assertTrue(0.0 < value)
                self.assertTrue(value < 1.00000000001)

            self.assertTrue(0.99999999999 < values_sum)
            self.assertTrue(values_sum < 1.00000000001)

        # check all page rank values sum is 1.0
        page_rank_values = pageRank.calculate_page_rank(matrix, "matrix")
        for value in page_rank_values:
            self.assertTrue(0.0 < value)
            self.assertTrue(value < 1.00000000001)

        total_page_rank = sum(page_rank_values)
        self.assertTrue(0.99999999999 < total_page_rank)
        self.assertTrue(total_page_rank < 1.00000000001)

        # check all page rank values sum is 1.0 (the presission is not equal)
        eigen_page_rank_values = pageRank.calculate_page_rank(matrix, "eigen")
        total_page_rank_eigen = sum(eigen_page_rank_values)
        for value in eigen_page_rank_values:
            self.assertTrue(0.0 < value)
            self.assertTrue(value < 1.00000000001)

        self.assertTrue(0.99999 < total_page_rank_eigen)
        self.assertTrue(total_page_rank_eigen < 1.000001)

    def test_page_rank_properties_with_1000_nodes_by_matrix_and_random_surfer(self):
        file = open("../page_rank_files/notre_dam_graph.txt", "r")
        file.readline()
        nodes = 100
        page_graph = np.zeros([nodes, nodes])

        # Iterate edges in file and add them to the graph
        for edge in file:
            source = int(edge.split()[0])
            dest = int(edge.split()[1])
            if source < nodes and dest < nodes:
                page_graph[int(source)][int(dest)] = 1

        pageRank = PageRank()

        # check all rows have 1.0 as sum
        matrix = pageRank.build_matrix(page_graph)
        for row in matrix:
            values_sum = sum(row.A[0])

            for value in row.A[0]:
                self.assertTrue(0.0 < value)
                self.assertTrue(value < 1.00000000001)

            self.assertTrue(0.99999999999 < values_sum)
            self.assertTrue(values_sum < 1.00000000001)

        # check all page rank values sum is 1.0
        page_rank_values = pageRank.calculate_page_rank(matrix, "matrix")
        for value in page_rank_values:
            self.assertTrue(0.0 < value)
            self.assertTrue(value < 1.00000000001)

        total_page_rank = sum(page_rank_values)
        self.assertTrue(0.99999999999 < total_page_rank)
        self.assertTrue(total_page_rank < 1.00000000001)

        # check all page rank values sum is 1.0 (the presission is not equal)
        eigen_page_rank_values = pageRank.calculate_page_rank(matrix, "random")
        total_page_rank_eigen = sum(eigen_page_rank_values)
        for value in eigen_page_rank_values:
            self.assertTrue(0.0 < value)
            self.assertTrue(value < 1.00000000001)

        self.assertTrue(0.9999 < total_page_rank_eigen)
        self.assertTrue(total_page_rank_eigen < 1.00001)


if __name__ == '__main__':
    unittest.main()
