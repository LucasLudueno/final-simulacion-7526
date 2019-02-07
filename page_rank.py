import sys
import json
import numpy as np

from time import time
from PageRank import PageRank

DEFAULT_MATRIX_DIM = 2000

def main(graph_file, convergence_method = "matrix", nodes_count = DEFAULT_MATRIX_DIM):
    file = open(graph_file, "r")
    nodes_analysis = {}
    nodes = int(file.readline())
    if nodes > nodes_count:
        nodes = nodes_count
    graph = np.zeros([nodes, nodes], dtype=np.uint8)

    # Iterate edges in file and add them to the graph
    print "Loading Graph..."
    for edge in file:
        source = int(edge.split()[0])
        dest = int(edge.split()[1])
        if source < nodes and dest < nodes:
            graph[int(source)][int(dest)] = 1

            if nodes_analysis.has_key(dest):
                nodes_analysis[dest]["links"] = nodes_analysis[dest]["links"] + 1
            else:
                nodes_analysis[dest] = { "links": 1 }

    # Calculate the page rank for each node
    print "Making Page Rank graph..."
    pageRank = PageRank()
    markov_matrix = pageRank.build_matrix(graph)

    print "Calculating Page Rank values..."
    page_rank_values = pageRank.calculate_page_rank(markov_matrix, convergence_method)

    print "Saving files..."
    with open(str(graph_file) + ".matrix.json", "w") as file:
        file.write(json.dumps(markov_matrix.getA().tolist()))
    
    with open(str(graph_file) + ".page_rank.json", "w") as file:
        file.write(json.dumps(page_rank_values))

    for x in xrange(len(page_rank_values)):
        if nodes_analysis.has_key(x):
            nodes_analysis[x]["rank"] = page_rank_values[x]
        else:
            nodes_analysis[x] = { "rank": page_rank_values[x], "links": 0  } 

    print "TOP 10 web pages"
    sorted_nodes = sorted(nodes_analysis.iteritems(), key=lambda (k,v): v["rank"], reverse=True)

    for key, value in sorted_nodes[0:10]:
        print "Node: " + str(key) + " - Page Rank: " + str(value["rank"]) + " - Incoming links count: " + str(value["links"])


if __name__ == "__main__":
    convergence_method = "matrix"
    nodes_count = 2000
    if len(sys.argv) == 4:
        convergence_method = sys.argv[2]
        nodes_count = int(sys.argv[3])
    if len(sys.argv) == 3:
	    convergence_method = sys.argv[2]
    sys.exit(main(sys.argv[1], convergence_method, nodes_count))
