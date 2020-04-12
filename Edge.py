class Edge:

    def __init__(self, startNode , endNode):
        self.startNode = startNode
        self.endNode   = endNode

    def get_startNode(self):
        return self.startNode

    def get_endNode(self):
        return self.endNode


    def get_startNode_name(self):
        return self.startNode.name


    def get_endNode_name(self):
        return self.endNode.name

