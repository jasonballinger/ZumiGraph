class Node:

    def __init__(self, n, p):
        self.name = n
        self.position = p
        self.visited = False
        self.edges = []

    def get_name(self):
        return self.name

    def get_edges(self):
        return self.edges


class Edge:

    def __init__(self, eName, startNode, endNode, alpha, beta, road_length):
        self.edgeName = eName
        self.startNode = startNode
        self.endNode = endNode
        self.startNodeDirToEndNode = alpha
        self.endNodeDirToStartNode = beta
        self.road_length = road_length

    def get_edgeName(self):
        return self.edgeName

    def get_startNode(self):
        return self.startNode

    def get_endNode(self):
        return self.endNode

    def get_startNode_name(self):
        return self.startNode.name

    def get_endNode_name(self):
        return self.endNode.name

    def get_startNodeDirToEndNode(self):
        return self.startNodeDirToEndNode

    def get_endNodeDirToStartNode(self):
        return self.endNodeDirToStartNode


class Graph:
    def __init__(self):
        self.nodes_dict = None
        self.edges_dict = None

    def create_simple(self):
        node_names = ['x', 'a', 's', 'b']
        node_pos = [(0, 10), (-10, 0), (0, 0), (10, 0)]
        nodes_dict = {}

        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value

        edges_dict = {}
        e1 = Edge("e1", nodes_dict['s'], nodes_dict['x'], 90, 270, 10)
        e2 = Edge("e2", nodes_dict['a'], nodes_dict['s'], 0, 180, 10)
        e3 = Edge("e3", nodes_dict['b'], nodes_dict['s'], 180, 0, 10)

        edges_dict['sx'] = e1
        edges_dict['as'] = e2
        edges_dict['bs'] = e3

        # add e1 to both vertices
        nodes_dict['s'].edges.append(e1)
        nodes_dict['x'].edges.append(e1)

        # add e2 to both vertices
        nodes_dict['a'].edges.append(e2)
        nodes_dict['s'].edges.append(e2)

        # add e3 to both vertices
        nodes_dict['b'].edges.append(e3)
        nodes_dict['s'].edges.append(e3)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict

    def create_simple_different_road_lengths(self):
        node_names = ['x', 'a', 's', 'b']
        node_pos = [(0, 8), (5, 0), (0, 0), (2, 0)]
        nodes_dict = {}

        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value

        edges_dict = {}
        e1 = Edge("e1", nodes_dict['s'], nodes_dict['x'], 90, 270, 8)
        e2 = Edge("e2", nodes_dict['a'], nodes_dict['s'], 0, 180, 5)
        e3 = Edge("e3", nodes_dict['b'], nodes_dict['s'], 180, 0, 2)

        edges_dict['sx'] = e1
        edges_dict['as'] = e2
        edges_dict['bs'] = e3

        # add e1 to both vertices
        nodes_dict['s'].edges.append(e1)
        nodes_dict['x'].edges.append(e1)

        # add e2 to both vertices
        nodes_dict['a'].edges.append(e2)
        nodes_dict['s'].edges.append(e2)

        # add e3 to both vertices
        nodes_dict['b'].edges.append(e3)
        nodes_dict['s'].edges.append(e3)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict

    def create_simple_different_angles(self):
        # 100 = 25 + x^2
        # x^2 = 100 - 25
        # x   = square_root(75)
        x = math.sqrt(75)

        node_names = ['x', 'a', 's', 'b']
        node_pos = [(0, 10), (-x, 5), (0, 0), (x, 5)]
        nodes_dict = {}

        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value

        edges_dict = {}
        e1 = Edge("e1", nodes_dict['s'], nodes_dict['x'], 90, 270, 10)  # input hyp.
        e2 = Edge("e2", nodes_dict['a'], nodes_dict['s'], 315, 135, 10)
        e3 = Edge("e3", nodes_dict['b'], nodes_dict['s'], 225, 45, 10)

        edges_dict['sx'] = e1
        edges_dict['as'] = e2
        edges_dict['bs'] = e3

        # add e1 to both vertices
        nodes_dict['s'].edges.append(e1)
        nodes_dict['x'].edges.append(e1)

        # add e2 to both vertices
        nodes_dict['a'].edges.append(e2)
        nodes_dict['s'].edges.append(e2)

        # add e3 to both vertices
        nodes_dict['b'].edges.append(e3)
        nodes_dict['s'].edges.append(e3)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict

    # Mystery Graph CODE
    def mystery_graph(self):
        node_names = ['x', 'a', 's', 'b', 'y']
        node_pos = [(-10, 10), (0, 10), (0, 0), (0, -10), (10, -10)]
        nodes_dict = {}

        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value

        edges_dict = {}

        e1 = Edge("e1", nodes_dict['a'], nodes_dict['x'], 180, 0, 10)
        e2 = Edge("e2", nodes_dict['s'], nodes_dict['x'], 135, 315, 10)
        e3 = Edge("e3", nodes_dict['a'], nodes_dict['s'], 270, 90, 10)
        e4 = Edge("e4", nodes_dict['b'], nodes_dict['s'], 90, 270, 10)
        e5 = Edge("e5", nodes_dict['s'], nodes_dict['y'], 315, 135, 10)
        e6 = Edge("e6", nodes_dict['b'], nodes_dict['y'], 0, 180, 10)

        edges_dict['sx'] = e1
        edges_dict['sx'] = e2
        edges_dict['as'] = e3
        edges_dict['bs'] = e4
        edges_dict['sy'] = e5
        edges_dict['by'] = e6

        # Node/Vertex 'S' add, all the edges
        nodes_dict['s'].edges.append(e2)
        nodes_dict['s'].edges.append(e3)
        nodes_dict['s'].edges.append(e4)
        nodes_dict['s'].edges.append(e5)

        # Node/Vertex 'A' add, all the edges
        nodes_dict['a'].edges.append(e1)
        nodes_dict['a'].edges.append(e3)

        # Node/Vertex 'B' add, all the edges
        nodes_dict['b'].edges.append(e4)
        nodes_dict['b'].edges.append(e6)

        # Node/Vertex 'Y' add, all the edges
        nodes_dict['y'].edges.append(e5)
        nodes_dict['y'].edges.append(e6)

        # Node/Vertex 'X' add, all the edges
        nodes_dict['x'].edges.append(e2)
        nodes_dict['x'].edges.append(e1)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict

    def create_complex(self):
        node_names = ['x', 'y', 'z', 'a', 's', 'b']
        node_pos = [(-5, 5), (0, 5), (5, 5), (-5, 0), (0, 0), (5, 0)]

        nodes_dict = {}
        # Create nodes and add them to the dictionary
        for index in range(0, len(node_names)):
            key = node_names[index]
            value = Node(node_names[index], node_pos[index])
            nodes_dict[key] = value
        edges_dict = {}

        e1 = Edge("e1", nodes_dict['x'], nodes_dict['y'], 0, 180, 5)
        e2 = Edge("e2", nodes_dict['y'], nodes_dict['z'], 0, 180, 5)
        e3 = Edge("e3", nodes_dict['s'], nodes_dict['y'], 90, 270, 5)
        e4 = Edge("e4", nodes_dict['s'], nodes_dict['z'], 45, 225, 5)
        e5 = Edge("e5", nodes_dict['b'], nodes_dict['z'], 90, 270, 5)
        e6 = Edge("e6", nodes_dict['a'], nodes_dict['s'], 0, 180, 5)
        e7 = Edge("e7", nodes_dict['s'], nodes_dict['b'], 0, 180, 5)

        edges_dict['xy'] = e1
        edges_dict['yz'] = e2
        edges_dict['sy'] = e3
        edges_dict['sz'] = e4
        edges_dict['bz'] = e5
        edges_dict['as'] = e6
        edges_dict['sb'] = e7

        # add e1 to both vertices
        nodes_dict['x'].edges.append(e1)
        nodes_dict['y'].edges.append(e1)
        # add e2 to both vertices
        nodes_dict['y'].edges.append(e2)
        nodes_dict['z'].edges.append(e2)
        # add e3 to both vertices
        nodes_dict['s'].edges.append(e3)
        nodes_dict['y'].edges.append(e3)
        # add e4 to both vertices
        nodes_dict['s'].edges.append(e4)
        nodes_dict['z'].edges.append(e4)
        # add e5 to both vertices
        nodes_dict['b'].edges.append(e5)
        nodes_dict['z'].edges.append(e5)
        # add e6 to both vertices
        nodes_dict['a'].edges.append(e6)
        nodes_dict['s'].edges.append(e6)
        # add e7 to both vertices
        nodes_dict['s'].edges.append(e7)
        nodes_dict['b'].edges.append(e7)

        # set class vars
        self.nodes_dict = nodes_dict
        self.edges_dict = edges_dict

    def search(self, startChar, destinationChar):
        startNode = self.nodes_dict[startChar]
        destinationNode = self.nodes_dict[destinationChar]
        queue = []
        queue.append((startNode, []))

        while (len(queue) > 0):

            currNode, currRoute = queue.pop(0)
            currNode.visited = True

            if currNode == destinationNode:
                print("FOUND")
                return currRoute

            for edge in currNode.edges:
                # print("Examining edge from ->", edge.get_startNode_name(), "<- to ->", edge.get_endNode_name(), "<-" )
                if edge.startNode != currNode and edge.startNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append((edge, edge.get_endNodeDirToStartNode()))
                    # new_route.append(  edge.startNode )
                    queue.append((edge.startNode, new_route))
                elif edge.endNode != currNode and edge.endNode.visited == False:
                    new_route = currRoute.copy()
                    new_route.append((edge, edge.get_startNodeDirToEndNode()))
                    # new_route.append(edge.endNode)
                    queue.append((edge.endNode, new_route))

        return "FAILED"
