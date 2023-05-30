
import sys
import time
import numpy as np

from hamiltonianCycleBacktracking import *

sys.path.append('../logic')
from utils import *
from logic import *

# This function is invoked when the python script is run directly and not imported
if __name__ == '__main__':
  results_file = "results.csv"
  output = open(results_file, "a")
  line = "Type, Nodes, Edges, Time(s), STD\n"
  # output.write(line)

  # This is for reading in the arguments.
  if len(sys.argv) != 2:
    print("Usage: %s <filepath>" % sys.argv[0])
    sys.exit(1)

  # Read Graph
  filepath = sys.argv[1]
  n_nodes, n_edges, graph = get_graph_from_file(filepath)
  graph_encoded = encode_graph(n_nodes, n_edges, graph)

  # Logic approach
  times = []
  for i in range(10):
    ti = time.time()
    generateClausesFile(n_nodes, graph_encoded)
    res = runSATsolver()
    tf = time.time()
    times.append(tf - ti)

  mean_time = sum(times)/len(times)
  std = np.std(times)
  line = "Logic, " + str(n_nodes) + ", " + str(n_edges) + ", " + str(
      mean_time) + ", " + str(std) + "\n"
  output.write(line)

  # Recursive approach
  times = []
  for i in range(10):
    ti = time.time()
    g = Graph(n_nodes)
    g.graph = graph_encoded
    g.hamCycle()
    tf = time.time()
    times.append(tf - ti)

  mean_time = sum(times)/len(times)
  std = np.std(times)
  line = "Recursive, " + str(n_nodes) + ", " + str(n_edges) + ", " + str(
      mean_time) + ", " + str(std) + "\n"
  output.write(line)

  output.close()


