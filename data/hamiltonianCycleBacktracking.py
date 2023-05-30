
# Python program for solution of
# hamiltonian cycle problem
# Solution from https://www.geeksforgeeks.org/hamiltonian-cycle/
# This algorithm is not part of the assigment and was used just to compare
# the perfomace using backtracking compared with the boolean approach.

import sys

sys.path.append('../logic')
from utils import *

class Graph():
  def __init__(self, vertices):
    self.graph = [[0 for column in range(vertices)]
                  for row in range(vertices)]
    self.V = vertices

  ''' Check if this vertex is an adjacent vertex
      of the previously added vertex and is not
      included in the path earlier '''
  def isSafe(self, v, pos, path):
    # Check if current vertex and last vertex
    # in path are adjacent
    if self.graph[ path[pos-1] ][v] == 0:
      return False

    # Check if current vertex not already in path
    for vertex in path:
      if vertex == v:
        return False

    return True

  # A recursive utility function to solve
  # hamiltonian cycle problem
  def hamCycleUtil(self, path, pos):

    # base case: if all vertices are
    # included in the path
    if pos == self.V:
      # Last vertex must be adjacent to the
      # first vertex in path to make a cycle
      if self.graph[ path[pos-1] ][ path[0] ] == 1:
        return True
      else:
        return False

    # Try different vertices as a next candidate
    # in Hamiltonian Cycle. We don't try for 0 as
    # we included 0 as starting point in hamCycle()
    for v in range(1,self.V):

      if self.isSafe(v, pos, path) == True:

        path[pos] = v

        if self.hamCycleUtil(path, pos+1) == True:
          return True

        # Remove current vertex if it doesn't
        # lead to a solution
        path[pos] = -1

    return False

  def hamCycle(self):
    path = [-1] * self.V

    ''' Let us put vertex 0 as the first vertex
        in the path. If there is a Hamiltonian Cycle,
        then the path can be started from any point
        of the cycle as the graph is undirected '''
    path[0] = 0

    if self.hamCycleUtil(path,1) == False:
      print ("Solution does not exist\n")
      return False

    #self.printSolution(path)
    return True

  def printSolution(self, path):
    print ("Solution Exists: Following",
           "is one Hamiltonian Cycle")
    for vertex in path:
      print (vertex, end = " ")
    print (path[0], "\n")

# This function is invoked when the python script is run directly and not imported
if __name__ == '__main__':
  # This is for reading in the arguments.
  if len(sys.argv) != 2:
    print("Usage: %s <filepath>" % sys.argv[0])
    sys.exit(1)

  filepath = sys.argv[1]
  n_nodes, n_edges, graph = get_graph_from_file(filepath)
  graph_encoded = encode_graph(n_nodes, n_edges, graph)

  g = Graph(n_nodes)
  g.graph = graph_encoded
  # Print the solution
  g.hamCycle()