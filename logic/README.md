# toc-project

## Project setup

Install Z3:

On Linux you can use:

```
sudo apt-get -y install z3
```

On MacOS:

```
brew install z3
```

## Execute logic processor

Execute:

```
python3 logic.py filepath
```

Where filepath is the path for a txt file describing an undirected graph, in this file in the first line we have the number of nodes  N and the
number of edges E, and following we have the list of edges. The nodes have to be represented as an integer number from zero to N-1. A possible graph would have the following structure:

```
N E
n1 n2
n2 n1
n2 n3
...
```


## Example

Inside the logic directory, we can execute:

```
python3 logic.py ../graphs/g1.txt
```

The graph will be encoded and Z3 will try to find a Hamiltonian Cycle to this graph. The structure of this graph is:

```
6 6
0 1
1 2
2 3
3 4
4 5
5 0
```

After the reasoning, if there is a path it would be saved in the output directory, with the same name from the original graph.
In this case, the output would be the following path:

```
4 5 0 1 2 3 
```

So from node 4 we can go to node 5. From node 5 to node 0 and so on, forming the cycle.
