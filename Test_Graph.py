import unittest
from Graph import Graph

class MyTestCase(unittest.TestCase):

    def test_print_coordinates_of_simple_nodes(self):
        graphObject = Graph()
        graphObject.create_simple()
        nodes = graphObject.nodes_dict

        for key in nodes:
            print(key, 'is assigned to coordinate ->', nodes[key].position)

    def test_print_edges_of_node_s(self):
        graphObject = Graph()
        graphObject.create_simple()
        nodes = graphObject.nodes_dict

        s_edges = nodes['s'].get_edges()

        for e in s_edges:
            print("start==",e.get_startNode_name() , end='')
            print("   ~~  end==",e.get_endNode_name())



if __name__ == '__main__':
    unittest.main()
