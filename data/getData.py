
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
  output = open(results_file, "w")
  line = "Type, Nodes, Edges, Graph, Time(s), STD\n"
  output.write(line)
  output.close()
  output = open(results_file, "a")

  format_data = "{}, {}, {}, {}, {:.8f},  {:.8f}\n"

  for j in range(1, 3):
    filepath = "../graphs/g" + str(j) + ".txt"

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

    res = runSATsolver()
    is_satisfiable = "Unsatisfiable"
    if res[0] == "s SATISFIABLE" or res[0] == "sat":
      is_satisfiable = "Satisfiable"

    mean_time = sum(times)/len(times)
    std = np.std(times)
    line = format_data.format("Logic", n_nodes, n_edges, is_satisfiable,
                              mean_time, std)
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
    line = format_data.format("Recursive", n_nodes, n_edges, is_satisfiable,
                              mean_time, std)
    output.write(line)

  output.close()


