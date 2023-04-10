class Graph:
    """
    Graph is a class for weighted graph
    the attributes are: 
        __nodes : the list of nodes in the graph
        __adjmatrix : the adjacency matrix that show the distance between two nodes, if there is no edge that connects the nodes, the value will be -1
    """
    def __init__(self, nodes, adjmatrix):
        """
        initialize a new graph
        """
        self.__nodes = nodes
        self.__adjmatrix = adjmatrix
    
    def adjmatrix(self):
        """
        adjmatrix getter
        """
        return self.__adjmatrix
    
    def nodes(self):
        """
        nodes getter
        """
        return self.__nodes
    
    def show(self):
        """
        prints the graph:
            1. print the list of nodes
            2. print the adjacency matrix
        """
        for node in self.__nodes:
            node.show()
        # for row in self.__adjmatrix:
        #     for col in row:
        #         print(col, end=" ")
        #     print()
