class Node:

    def __init__(self, n, p):
        self.name       = n
        self.position   = p
        self.visited    = False
        self.edges      = []


    def get_name(self):
        return self.name


    def get_edges(self):
        return self.edges