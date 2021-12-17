from collections import defaultdict
from node import Node
from graph import Graph

if __name__ == "__main__":

    # Step1: Initialize nodes and add to graph
    num_vertices = 12
    g = Graph(num_vertices)

    for i in range(1, num_vertices+1):
        n = Node(i, 1)
        g.add_node(n)

    #Step2: Add edges to graph
    adjacency_list = [(1, 2), (1, 6), (2, 6), (2, 3), (2, 4), (3, 4), (4, 5), (5, 6), (8, 8), (7, 12), (8, 12), (8, 9), (8, 10), (9, 10), (10, 11), (11, 12)]
    for edge in adjacency_list:
        g.add_edge(edge[0], edge[1])

    # Step3: iterate until number of colors used in two consecutive iterations dont change/increase.
    prev_unique_color_count = 1
    ite = 0
    while True:
        #print("Iteration: {}".format(ite))

        node_list = g.get_nodes()
        edge_list = g.get_edge_list()
        for node in node_list:
            for neighnour_node in edge_list[node.get_id()]:
                n_color = g.get_node_by_id(neighnour_node).get_color()
                #print("Start: ", neighnour_node, n_color)
                node.update_neighbour_color_tuple(n_color)

        # Count unique neighbour tuples
        all_neighbour_tuples = defaultdict(list)
        for node in node_list:
            n_tuple = node.get_neighbour_color_tuple()
            all_neighbour_tuples[n_tuple['prev_color']].append((node.get_id(), n_tuple['neigh_color']))

        color_counter = 0
        color_wise_unique_tuples = defaultdict(list)
        unique_tupidx_color_map = defaultdict(list)
        for _, entry in enumerate(all_neighbour_tuples.items()):
            p_col = entry[0]
            n_list = entry[1]
            for nid_tup in n_list:
                node_id = nid_tup[0]
                tup = nid_tup[1]
                if tup in color_wise_unique_tuples[p_col]:
                    #print(node_id, color_counter)
                    pol_idx = color_wise_unique_tuples[p_col].index(tup)
                    tup_color_id = unique_tupidx_color_map[p_col][pol_idx]
                    g.get_node_by_id(node_id).set_color(tup_color_id)
                else:
                    color_counter += 1
                    #print(node_id, color_counter)
                    g.get_node_by_id(node_id).set_color(color_counter)
                    color_wise_unique_tuples[p_col].append(tup)
                    unique_tupidx_color_map[p_col].append(color_counter)
                    
        ite += 1

        if color_counter == prev_unique_color_count:
            print("Stablized partition!")
            #g.print_graph()
            g.one_wl_equivalence()
            break
        else:
            prev_unique_color_count = color_counter
            g.reset_neighbour_tuples()