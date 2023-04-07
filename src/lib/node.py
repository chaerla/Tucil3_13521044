class Node:
    def __init__(self, name, latitude, longitude):
        self.__name = name
        self.__latitude = latitude
        self.__longitude = longitude
    
    def latitude(self):
        return self.__latitude
    
    def longitude(self):
        return self.__longitude
    
    def show(self):
        print(self.__name + " (" + str(self.__longitude) + ", " + str(self.__latitude) + ")")
        
