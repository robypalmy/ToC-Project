def get_graph_from_file(filename):
  file = open(filename,'r')

  line = file.readline()
  graph_info_list = line.split()
  n_nodes = int(graph_info_list[0])
  n_edges = int(graph_info_list[-1])

  edges = []
  for i in range(n_edges):
    line = file.readline()
    edges.append([int(x) for x in line.split()])

  file.close()

  return n_nodes, n_edges, edges

if __name__ == '__main__':
  filename = "../graphs/g1.txt"
  n, e, edges = get_graph_from_file(filename)