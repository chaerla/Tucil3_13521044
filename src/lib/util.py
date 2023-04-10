from lib.graph import *
from lib.node import *
import math

def calc_haversine_dist(pos1: Node, pos2: Node):
    """
    calculate the haversine distance between two nodes
    """
    r = 6371  # radius of the Earth in kilometers
    phi1 = math.radians(pos1.latitude())
    phi2 = math.radians(pos2.latitude())
    delta_phi = math.radians(pos2.latitude() - pos1.latitude())
    delta_lambda = math.radians(pos2.longitude() - pos1.longitude())
    a = math.sin(delta_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    return r*c

def read_graph_from_file(file_name):
    """
    reads and parses a graph from a file
    """
    f = open(f"test/{file_name}", "r") # should run from root
    lines = f.readlines()

    nodes_count = int(lines[0])
    node_list = []
    adjmatrix = []

    line_idx = 1
    for i in range (nodes_count):
        name = lines[line_idx].strip("\n")
        pos = lines[line_idx+1].split(",")
        latitude = pos[0]
        longitude = pos[1].strip("\n")
        node = Node(i, name, float(latitude), float(longitude),0)
        node_list.append(node)
        line_idx+= 2
    
    curr_node = 0
    for i in range (nodes_count):
        curr_node_neighbours = lines[line_idx].strip("\n").split(" ")
        # print(curr_node_neighbours)
        for j in range (len(curr_node_neighbours)):
            # if (int(curr_node_neighbours[j]) == 1):
            #     curr_node_neighbours[j] = calc_haversine_dist(node_list[curr_node], node_list[j])
            # else:
            #     curr_node_neighbours[j] = -1
            if(float(curr_node_neighbours[j]) != float(0)):
                curr_node_neighbours[j] = float(curr_node_neighbours[j])
            else:
                curr_node_neighbours[j] = float(-1)

        adjmatrix.append(curr_node_neighbours)
        line_idx+=1
        curr_node+=1
    
    return Graph(node_list, adjmatrix)


def get_node_idx_from_name(node_name: str, graph: Graph):
    for i in range(len(graph.nodes())):
        if(graph.nodes()[i].name() == node_name):
            return graph.nodes()[i].index()
    return -1