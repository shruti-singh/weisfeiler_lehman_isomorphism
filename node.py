from collections import defaultdict 

class Node:

    def __init__(self, id, color):
        self.id = id
        self.color = color
        self.neighbour_color_tuple = {'prev_color': color, 'neigh_color': defaultdict(int)}
        return

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color

    def get_id(self):
        return self.id

    def get_neighbour_color_tuple(self):
        return self.neighbour_color_tuple

    def update_neighbour_color_tuple(self, neigh_color):
        self.neighbour_color_tuple['neigh_color'][neigh_color] += 1
    
    def reset_neighbour_color_tuple(self):
        self.neighbour_color_tuple = {'prev_color': self.color, 'neigh_color': defaultdict(int)}
