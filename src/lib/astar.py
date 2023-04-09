from lib.graph import *
from lib.node import *
from lib.util import * 

def astar(start: Node, goal: Node, graph: Graph):
    """
    A function to find the shortest path between start and goal using A* algorithm
    returns a dictionary:
    {
        "cost"      : {the cost of the path}
        "path"      : {the shortest path between the nodes}
        "success"   : {whether or not there's a path connecting the start and goal}
    }
    """
    # add heuristic distance for every node in graph
    for i in range(len(graph.nodes())):
        node = graph.nodes()[i]
        heuristic = calc_haversine_dist(node, goal)
        graph.nodes()[i].set_heuristic(heuristic)

    queue = [] #priority queue that stores the nodes to be visited

    """ 
    queue element is a dictionary consist of:  
    {
        "node"              : {the node to be visited}
        "cost_so_far"       : {the cost to visit the node}
        "path"              : {the path to reach the node}
        "prediction_cost"   : {cost prediction from the start node to the goal node with heuristics}
    }
    prediction_cost = cost_so_far + heuristic
    """
    first_entry = {
        "node"              : start,
        "cost_so_far"       : 0,
        "path"              : [start], 
        "prediction_cost"   : start.heuristic()
    }
    queue.append(first_entry)

    # initialize the answer to the starting node
    answer = {
        "cost"      : 0,
        "path"      : 0,
        "success"   : False
    }

    while(len(queue) > 0):
        queue = sorted(queue, key=lambda x: x["prediction_cost"])

        # the current node to check
        curr = {
            "node"              : queue[0]["node"],
            "cost_so_far"       : queue[0]["cost_so_far"],
            "path"              : queue[0]["path"],
            "prediction_cost"   : queue[0]["prediction_cost"]
        }

        # check if current node is goal, the first found is guaranteed to be the minimum
        if(curr["node"].index() == goal.index()):
            answer = {
                "cost": curr["cost_so_far"],
                "path": curr["path"],
                "success": True
            }
            return answer 

        # expands the node, push all its neighbours to the priority queue
        for i in range(len(graph.adjmatrix()[curr["node"].index()])):
            if(graph.adjmatrix()[curr["node"].index()][i] != -1):

                # if node that want to be visited already in curr path, don't add it to queue (to limit the search)
                if(graph.nodes()[i] not in curr["path"]):
                    cost_so_far = curr["cost_so_far"] + graph.adjmatrix()[curr["node"].index()][i]
                    temp = {
                        "node"              : graph.nodes()[i],
                        "path"              : curr["path"] + [graph.nodes()[i]],
                        "cost_so_far"       : cost_so_far,
                        "prediction_cost"   : cost_so_far + graph.nodes()[i].heuristic()
                    }
                    queue.append(temp)
                
        # remove the first element from the queue
        del queue[0]

    # if reach this point, then the answer must be unsuccess
    return answer