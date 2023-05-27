# toc-project

## Project setup

Install Z3:

On Linux you can use:

'''
sudo apt-get -y install z3
'''

On MacOS:

'''
brew install z3
'''

## Execute logic processor

Execute:

'''
python3 logic.py filepath
'''

Where filepath is the path for a txt file describing an undirected graph, in this file in the first line we have the number of nodes  N and the 
number of edges E, and following we have the list of edges. The nodes have to be represented as an integer number from zero to N-1. 
