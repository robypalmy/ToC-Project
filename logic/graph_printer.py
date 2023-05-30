import networkx as nx
import matplotlib.pyplot as plt

def function(filename):
    output_file_name = filename.replace("graphs/", "graphs/outputs/")
    with open(filename, 'r') as file:
        data = file.readlines()
    with open(output_file_name, 'r') as file:
        output_file = file.readlines()
    # Extract the number of nodes and edges
    N, E = map(int, data[0].split())

    # Create an empty graph
    G = nx.Graph()

    # Add edges to the graph
    for line in data[1:]:
        n1, n2 = map(int, line.split())
        G.add_edge(n1, n2)

    # get the first line of the output file without the \n
    sat_output = output_file[0][:-1]
    print(sat_output)
    # color all nodes and edges
    color_map = ['lightblue'] * G.number_of_nodes() # N?
    edge_colors = ['black'] * E

    if sat_output == "SATISFIABLE":
        print("The graph has a Hamiltonian cycle.")
        # Extract the Hamiltonian cycle from the file
        hamiltonian_cycle = list(map(int, output_file[-1].split()))
        print(hamiltonian_cycle)
        # Color the nodes in the Hamiltonian cycle differently
        for i in range(len(hamiltonian_cycle)):
            node = hamiltonian_cycle[i]
            color_map[node] = 'red'

        # Color the edges in the Hamiltonian path differently
        for i in range(len(hamiltonian_cycle) - 1):
            n1, n2 = hamiltonian_cycle[i], hamiltonian_cycle[i + 1]
            if (n1, n2) in list(G.edges):
                edge_colors[list(G.edges).index((n1, n2))] = 'green'
            elif (n2, n1) in list(G.edges):
                edge_colors[list(G.edges).index((n2, n1))] = 'green'
        # color last and first node of the cycle
        n1, n2 = hamiltonian_cycle[0], hamiltonian_cycle[-1]
        if (n1, n2) in list(G.edges):
            edge_colors[list(G.edges).index((n1, n2))] = 'green'
        elif (n2, n1) in list(G.edges):
            edge_colors[list(G.edges).index((n2, n1))] = 'green'

    # Draw the graph
    pos = nx.spring_layout(G)  # Layout algorithm for node positioning
    nx.draw(G, pos, with_labels=True, node_color=color_map, edge_color=edge_colors)
    plt.title('Graph Visualization')
    # plt.show()
    # save the graph as a .png file
    plt.savefig('images/' + filename + '.png')
