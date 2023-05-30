import random

def generate_undirected_graph(N, E, output_file):
  nodes = list(range(N))
  edges = set()

  # Generate E unique random edges
  while len(edges) < E:
    node1 = random.choice(nodes)
    node2 = random.choice(nodes)
    if node1 != node2:
      edge = (min(node1, node2), max(node1, node2))
      edges.add(edge)

  # Write the graph to the output file
  with open(output_file, 'w') as file:
    file.write(f"{N} {E}\n")
    for edge in edges:
      file.write(f"{edge[0]} {edge[1]}\n")

def generate_graph_with_hamiltonian_cycle(N, E, output_file):
  if E < N or E > N * (N - 1) // 2:
    print("Invalid number of edges. The number of edges should be between N and N*(N-1)/2.")
    return

  nodes = list(range(N))
  edges = set()

  # Generate a Hamiltonian cycle
  cycle = list(range(N))
  random.shuffle(cycle)
  for i in range(N - 1):
    edge = (cycle[i], cycle[i + 1])
    edges.add(edge)
  edges.add((cycle[N - 1], cycle[0]))

  # Add remaining edges randomly
  while len(edges) < E:
    node1 = random.choice(nodes)
    node2 = random.choice(nodes)
    if node1 != node2 and (node1, node2) not in edges and (node2, node1) not in edges:
      edge = (node1, node2)
      edges.add(edge)

  # Write the graph to the output file
  with open(output_file, 'w') as file:
    file.write(f"{N} {E}\n")
    for edge in edges:
      file.write(f"{edge[0]} {edge[1]}\n")

if __name__ == '__main__':
  N = int(input("Input number of nodes in the graph: "))
  E = int(input("Input number of edges in the graph: "))
  filename = input("Input graph file name: ")
  print()
  print("Graphs type:")
  print("1 - Random Graph ")
  print("2 - Hamiltonian Cycle Graph ")
  type = int(input("Choose type of graph: "))

  if type == 1:
    generate_undirected_graph(N, E, filename)
  elif type == 2:
    generate_graph_with_hamiltonian_cycle(N, E, filename)