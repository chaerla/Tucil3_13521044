class Graph:

    def __init__(self, nodes, adjmatrix):
        self.__nodes = nodes
        self.__adjmatrix = adjmatrix

    def show(self):
        for node in self.__nodes:
            node.show()

        for row in self.__adjmatrix:
            for col in row:
                print(col, end=" ")
            print()
