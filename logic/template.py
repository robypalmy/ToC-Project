#!/usr/bin/env python3


import sys
from subprocess import Popen
from subprocess import PIPE
import re
import random
import os

gbi = 0
varToStr = ["invalid"]

def printClause(cl):
    print(map(lambda x: "%s%s" % (x < 0 and eval("'_'") or eval ("''"), varToStr[abs(x)]) , cl))

def varName(pigeon,hole):
    return "inHole({},{})".format(pigeon, hole)

def gvi(name):
    global gbi
    global varToStr
    gbi += 1
    varToStr.append(name)
    return gbi

def gen_vars(pigeons, holes):

    varMap = {}

    # Insert here the code to add mapping from variable numbers to readable variable names.
    # A single variable with a human readable name "var_name" is added, for instance, as follows:
    # varMap["var_name"] = gvi("var_name")
    # let's add another one.
    # varMap["var2_name"] = gvi("var2_name")

    for hole in range(0, holes):
        for pigeon in range(0, pigeons):
            varName = "inHole_" + str(pigeon) + "_" + str(hole)
            varMap[varName] = gvi(varName)

    return varMap

def genPigConstr(pigeons, holes, vars):

    clauses = []

    # Insert here the code to generate the clauses.  A single clause var_name | var2_name is added as follows
    for hole in range(0, holes):
        for pigeon_i in range(0, pigeons):
            for pigeon_j in range(pigeon_i + 1, pigeons):
                varName1 = "inHole_" + str(pigeon_i) + "_" + str(hole)
                varName2 = "inHole_" + str(pigeon_j) + "_" + str(hole)
                clauses.append([-vars[varName1], -vars[varName2]])

    for pigeon in range(0, pigeons):
        for hole_i in range(0, holes):
            for hole_j in range(hole_i + 1, holes):
                varName1 = "inHole_" + str(pigeon) + "_" + str(hole_i)
                varName2 = "inHole_" + str(pigeon) + "_" + str(hole_j)
                clauses.append([-vars[varName1], -vars[varName2]])

    for pigeon in range(0, pigeons):
        list_rules = []
        for hole in range(0, holes):
            varName = "inHole_" + str(pigeon) + "_" + str(hole)
            list_rules.append(varName)
        clauses.append(list_rules)

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
    #if not (os.path.isfile(SATsolver) and os.access(SATsolver, os.X_OK)):
    # if Z3 is installed with homebrew in the PATH env no need to explicitly specify the solver
    #    print "Set the path to SATsolver correctly on line 4 of this file (%s)" % sys.argv[0]
    #    sys.exit(1)

    # This is for reading in the arguments.
    if len(sys.argv) != 3:
        print("Usage: %s <pigeons> <holes>" % sys.argv[0])
        sys.exit(1)

    pigeons = int(sys.argv[1])
    holes = int(sys.argv[2])

    vars = gen_vars(pigeons, holes)

    rules = genPigConstr(pigeons, holes, vars)

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
        for f in facts:
            print(f)

