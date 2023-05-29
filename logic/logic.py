#!/usr/bin/env python3


import sys
from subprocess import Popen
from subprocess import PIPE
import re
import random
import os
from utils import *

gbi = 0
varToStr = ["invalid"]

def printClause(cl):
  print(map(lambda x: "%s%s" % (x < 0 and eval("'_'") or eval ("''"), varToStr[abs(x)]) , cl))

def varName(position, node):
  return "inPosition_{}_{}".format(position, node)

def gvi(name):
  global gbi
  global varToStr
  gbi += 1
  varToStr.append(name)
  return gbi

def gen_vars(n):
  varMap = {}
  for position in range(0, n):
    for node in range(0, n):
      varName1 = varName(str(position), str(node))
      varMap[varName1] = gvi(varName1)

  return varMap

def genPigConstr(n_nodes, vars, graph):
  clauses = []

  # Each position has to be occupied
  for position in range(n_nodes):
    clause = []
    for node in range(n_nodes):
      clause.append(vars[varName(str(position), str(node))])
    clauses.append(clause)

  # Each node has to appear in the path
  for node in range(n_nodes):
    clause = []
    for position in range(n_nodes):
      clause.append(vars[varName(str(position), str(node))])
    clauses.append(clause)

  # Position with no more than one node
  for position in range(0, n_nodes):
    for node_i in range(0, n_nodes):
      for node_j in range(node_i + 1, n_nodes):
        varName1 = varName(str(position), str(node_i))
        varName2 = varName(str(position), str(node_j))
        clauses.append([-vars[varName1], -vars[varName2]])

  # Node in just one position
  for node in range(0, n_nodes):
    for position_i in range(0, n_nodes):
      for position_j in range(position_i + 1, n_nodes):
        varName1 = varName(str(position_i), str(node))
        varName2 = varName(str(position_j), str(node))
        clauses.append([-vars[varName1], -vars[varName2]])

  # Two nodes in sequence need to have a edge
  for node_i in range(0, n_nodes):
    for node_j in range(0, n_nodes):
      if not graph[node_i][node_j]:
        for position in range(0, n_nodes):
          varName1 = varName(str(position), str(node_i))
          varName2 = varName(str((position + 1) % n_nodes), str(node_j))
          clauses.append([-vars[varName1], -vars[varName2]])

  return clauses


# A helper function to print the cnf header
def printHeader(n):
  global gbi
  return "p cnf {} {}".format(gbi, n)

# A helper function to print a set of clauses cls
def printCnf(cls):
  return "\n".join(map(lambda x: "%s 0" % " ".join(map(str, x)), cls))

# This function is invoked when the python script is run directly and not imported
if __name__ == '__main__':
  # This is for reading in the arguments.
  if len(sys.argv) != 2:
    print("Usage: %s <filepath>" % sys.argv[0])
    sys.exit(1)

  filepath = sys.argv[1]
  n_nodes, n_edges, graph = get_graph_from_file(filepath)
  graph_encoded = encode_graph(n_nodes, n_edges, graph)

  vars = gen_vars(n_nodes)
  rules = genPigConstr(n_nodes, vars, graph_encoded)

  head = printHeader(len(rules))
  rls = printCnf(rules)

  # here we create the cnf file for SATsolver
  fl = open("tmp_prob.cnf", "w")
  fl.write("\n".join([head, rls]))
  fl.close()

  # this is for runing SATsolver
  ms_out = Popen(["z3 tmp_prob.cnf"], stdout=PIPE, shell=True).communicate()[0]

  # SATsolver with these arguments writes the solution to a file called "solution".  Let's check it
  #res = open("solution", "r").readlines()
  res = ms_out.decode('utf-8')
  # Print output
  print(res)
  res = res.strip().split('\n')

  # if it was satisfiable, we want to have the assignment printed out
  if res[0] == "s SATISFIABLE":
    # First get the assignment, which is on the second line of the file, and split it on spaces
    # Read the solution
    asgn = map(int, res[1].split()[1:])
    # Then get the variables that are positive, and get their names.
    # This way we know that everything not printed is false.
    # The last element in asgn is the trailing zero and we can ignore it

    #Convert the solution to our names
    facts = map(lambda x: varToStr[abs(x)], filter(lambda x: x > 0, asgn))

    # Print the solution
    solution = ""
    for f in facts:
      print(f)
      fparts = f.split("_")
      solution += fparts[-1] + " "

    # Save the solution
    solution_filepath = filepath.replace("graphs/", "graphs/outputs/")
    output = open(solution_filepath, "w")
    output.write(solution)
    output.close()
