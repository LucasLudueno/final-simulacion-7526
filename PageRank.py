import numpy as np
from numpy.linalg import matrix_power

class PageRank:
    """ """

    def __init__(self, convergenceIterations = 50, normValue = 0.85 ):
       self.convergence_iterations = convergenceIterations
       self.matrix_normalization_value = normValue

    def build_matrix(self, linkGraph):
        norm_value = self.matrix_normalization_value
        # Build matrix given graph
        linkGraph = np.matrix(linkGraph)
        nodesCount = linkGraph.shape[0]

        # Fill Dangling nodes
        # For each node write in rows 1/N if there exist an outgoing node link. N outgoing links
        matrixWithoutDangling = []
        for row in linkGraph:
            outgoingLinksCount = sum(row.A[0])

            newMatrixRow = []
            if outgoingLinksCount == 0:
                # If there is a node with no outgoing links, complete all column with 1/N. N nodes
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

    def calculate_page_rank(self, matrix):
        iterations = self.convergence_iterations
        pagesCount = matrix.shape[0]

        # Initial page rank vector. All pages with same probability
        initial_page_rank = [1.0 / pagesCount for x in range(pagesCount)]

        # That operation represents: matrix ** N
        convergence_matrix = matrix_power(matrix, iterations)

        # The page rank value for any page
        page_rank_values = np.matmul(initial_page_rank, convergence_matrix)

        return page_rank_values.tolist()[0]
