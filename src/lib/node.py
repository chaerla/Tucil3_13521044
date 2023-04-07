class Node:
    """
    Node is a class for nodes in a graph
    This class has attributes:
        __name: the name of the node (location)
        __latitude: the latitude of the location
        __longitude: the longitude of the location
        __index: the index (acts as an id for the node)
    """
    def __init__(self, index, name, latitude, longitude):
        """
        initialize a Node
        """
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude
        self.__index = index
    
    def latitude(self):
        return self.__latitude
    
    def longitude(self):
        return self.__longitude
    
    def name(self):
        return self.__name

    def index(self):
        return self.__index
    
    def show(self):
        """
        prints a node with format
        {[index]} {name} ({latitude}, {longitude})
        """
        print("[" + str(self.__index) + "]" + self.__name + " (" + str(self.__longitude) + ", " + str(self.__latitude) + ")")
    
        
