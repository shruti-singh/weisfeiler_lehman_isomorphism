from collections import defaultdict

class Graph:

    def __init__(self, num_vertices):
        self.node_list = []
        self.edge_list = defaultdict(list)
        return
    
    def add_node(self, node):
        self.node_list.append(node)
        return

    def get_node_by_id(self, id):
        for node in self.node_list:
            if node.get_id() == id:
                return node
        return None

    def add_edge(self, src, target):
        self.edge_list[src].append(target)
        self.edge_list[target].append(src)
        return

    def print_graph(self):
        for node in self.node_list:
            print(node.get_id(), node.get_color(), node.get_neighbour_color_tuple())
        return

    def get_nodes(self):
        return self.node_list

    def get_edge_list(self):
        return self.edge_list

    def reset_neighbour_tuples(self):
        for node in self.node_list:
            node.reset_neighbour_color_tuple()

    def one_wl_equivalence(self):
        g1_colors = [x.get_color() for x in self.node_list[0: len(self.node_list)//2]]
        g2_colors = [x.get_color() for x in self.node_list[len(self.node_list)//2:]]

        if g1_colors == g2_colors:
            print("Graphs are 1-WL equivalent!")
        else:
            print("Graphs are not 1-WL equivalent. :(")
        return