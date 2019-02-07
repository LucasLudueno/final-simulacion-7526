import numpy as np
import random

from numpy.linalg import inv
from numpy import linalg as LA
from numpy.linalg import matrix_power

CONVERGENCE_ITERATIONS = 52
NORMALIZATION_VALUE = 0.85

class PageRank:
    """ Module that compute Page Rank for each node of a graph """

    def __init__(self, convergence_iterations = CONVERGENCE_ITERATIONS, norm_value = NORMALIZATION_VALUE ):
       self.convergence_iterations = convergence_iterations # iterations when algorithm converge
       self.matrix_normalization_value = norm_value         # value to normalize the matrix


    """ Given a graph of urls, builds a probabilistic matrix for the PageRank algorithm
    """
    def build_matrix(self, urls_graph):
        norm_value = self.matrix_normalization_value
        # Build matrix given graph
        urls_graph = np.matrix(urls_graph)
        nodesCount = urls_graph.shape[0]

        # Fill Dangling nodes
        # For each node write in rows 1/N if there exist an outgoing node link. N outgoing links
        matrixWithoutDangling = []
        for row in urls_graph:
            outgoingLinksCount = sum(row.A[0])

            newMatrixRow = []
            if outgoingLinksCount == 0:
                # If there is a node with no outgoing links, complete all rows with 1/N. N nodes
                newMatrixRow = [1.0 for x in range(nodesCount)]
            else:
                newMatrixRow = row.A[0]
            
            matrixWithoutDangling.append(newMatrixRow)

        matrixWithoutDangling = np.matrix(matrixWithoutDangling)

        # Transform in a Markov matrix
        markovMatrix = []
        for rowArray in matrixWithoutDangling:
            row = rowArray.A[0]
            outgoingLinksCount = sum(row)
            newMatrixRow = [float(value) / outgoingLinksCount for value in row]
            markovMatrix.append(newMatrixRow)
        markovMatrix = np.matrix(markovMatrix)

        # Complete the matrix with probabilities to other nodes 
        adaptedMatrix = np.multiply(markovMatrix, norm_value)

        onesMatrix = np.ones((nodesCount, nodesCount))
        additionalMatrix = np.multiply(onesMatrix, (1.0 - norm_value) / nodesCount)
        
        return adaptedMatrix + additionalMatrix


    """ Given a normalized matrix that represents an url graph, returns an array where
        each position represents a page in the row position of the matrix
    """
    def calculate_page_rank(self, matrix, convergence_type = "matrix"):
        if convergence_type == "matrix":
            return self.page_rank_by_matrix_mult(matrix)

        elif convergence_type == "random":
            return self.page_rank_by_random_surfer(matrix)

        return self.page_rank_by_eigen_matrix_mult(matrix)


    def page_rank_by_matrix_mult(self, matrix):
        iterations = self.convergence_iterations
        print "Iterations: " + str(iterations)

        pagesCount = matrix.shape[0]

        # Initial page rank vector. All pages with same probability
        initial_page_rank = [1.0 / pagesCount for x in range(pagesCount)]

        # That operation represents: matrix ** N
        convergence_matrix = matrix_power(matrix, iterations)

        # The page rank value for any page
        page_rank_values = np.matmul(initial_page_rank, convergence_matrix)
        return page_rank_values.tolist()[0]


    def page_rank_by_random_surfer(self, matrix):
        iterations = self.convergence_iterations
        pagesCount = matrix.shape[0]
        
        total_states_count = iterations * pagesCount
        print "Iterations: " + str(total_states_count)

        # Calculate the acum probabibility matrix per row
        prob_acum_matrix = np.zeros([pagesCount, pagesCount])
        for i in range(pagesCount):
            probabilities_acum = 0.0
            
            current_row = matrix[i].A[0]
            for j in range(pagesCount):
                current_value = current_row[j]
                probabilities_acum += current_value
                prob_acum_matrix[i][j] = probabilities_acum

        # Calculate the count of states over iterations
        current_state = 0 # we start from node 0
        page_rank_values = np.zeros([pagesCount])
        page_rank_values[current_state] += 1
        for it in xrange(total_states_count):
            current_row = prob_acum_matrix[current_state]
            random_value = random.random()

            for i in range(pagesCount):
                value = current_row[i]
                if value >= random_value:
                    current_state = i
                    page_rank_values[i] += 1
                    break
        
        # Calculate the page rank for each page
        page_rank_values = [float(value) / total_states_count for value in page_rank_values]
        return page_rank_values


    def page_rank_by_eigen_matrix_mult(self, matrix):
        iterations = self.convergence_iterations
        print "Iterations: " + str(iterations)

        pagesCount = matrix.shape[0]

        # Initial page rank vector. All pages with same probability
        initial_page_rank = [1.0 / pagesCount for x in range(pagesCount)]

        # Calculate eigen values and vectors
        w, v = LA.eig(matrix)
        eigen_values_vectors = []
        eigen_values = w
        
        cont = 0
        for column in v.T:
            eigen_values_vectors.append((eigen_values[cont], column))
            cont += 1

        eigen_values_vectors.sort(key=lambda tup: abs(tup[0]))

        # Calculate eigen value matrix
        eigen_vector_matrix = []
        eigen_value_matrix = np.zeros([pagesCount, pagesCount], dtype=complex)
        for i in xrange(len(eigen_values_vectors)):
            eigen_value_matrix[i][i] = eigen_values_vectors[i][0]
            eigen_vector_matrix.append(eigen_values_vectors[i][1].tolist()[0])
        
        eigen_vector_matrix = np.matrix(eigen_vector_matrix)
        eigen_vector_matrix = eigen_vector_matrix.T

        # That operation represents: matrix ** N
        convergence_eigen_matrix = matrix_power(eigen_value_matrix, iterations)

        # Calculate eigen vector matrix
        inverse_eigen_vector_matrix = inv(eigen_vector_matrix)

        # Calculate the result matrix: P * Dn * P-1
        partial_convergence_matrix = np.matmul(eigen_vector_matrix, convergence_eigen_matrix)
        convergence_matrix = np.matmul(partial_convergence_matrix, inverse_eigen_vector_matrix).real  

        # The page rank value for any page
        page_rank_values = np.matmul(initial_page_rank, convergence_matrix)
        return page_rank_values.tolist()[0]
