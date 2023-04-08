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
    queue.append({
        "node"              : start,
        "cost_so_far"       : 0,
        "path"              : [start], 
        "prediction_cost"   : start.heuristic() 
    })

    # initialize the answer to the starting node
    answer = {
        "cost"      : 0,
        "path"      : 0,
        "success"   : False
    }

    """ 
    initialize flag that will be used in the algorithm
        found               : to indicate whether the goal has been reached or not
        shortest_distance   : to indicate whether the cost to reach the goal has been minimum or not
        found_shortest      : to indicate whether the goal has been reached and the distance has been minimum or not
    """
    found = False
    shortest_distance = False
    found_shortest = found and shortest_distance

    while(len(queue) > 0 and not found_shortest):
        queue = sorted(queue, key=lambda x: x["prediction_cost"])

        # the current node to check
        curr = {
            "node"              : queue[0]["node"],
            "cost_so_far"       : queue[0]["cost_so_far"],
            "path"              : queue[0]["path"],
            "prediction_cost"   : queue[0]["prediction_cost"]
        }
        
        # check if the current node is the goal
        if(curr["node"].index() == goal.index()):
            found = True
            # check whether the cost is definitely minimum or not to make sure we found the minimum distance
            if(len(queue) > 1): # checks if the next element in the queue might return the shortest distance
                shortest_distance = (curr["cost_so_far"] <= queue[1]["prediction_cost"])
            else: # if curr is the last element in the queue then the cost must be minimum
                shortest_distance = True

            found_shortest = found and shortest_distance

            answer = {
                "cost"      : curr["cost_so_far"], 
                "path"      : curr["path"], 
                "success"   : found_shortest
            }

            if(found_shortest):
                return answer
        
        # checks whether the element currently in the queue is unlikely to produce a shorter distance than the previous one
        if(found):
            if(curr["prediction_cost"] > answer["cost"]):
                answer["success"] = True
                return answer

        # expands the node, push all its neighbours to the priority queue
        for i in range(len(graph.adjmatrix()[curr["node"].index()])):
            if(graph.adjmatrix()[curr["node"].index()][i] != -1):
                cost_so_far = curr["cost_so_far"]
                temp = {
                    "node"              : graph.nodes()[i],
                    "path"              : curr["path"] + [graph.nodes()[i]],
                    "cost_so_far"       : curr["cost_so_far"] + graph.adjmatrix()[curr["node"].index()][i],
                    "prediction_cost"   : cost_so_far + graph.nodes()[i].heuristic()
                }
                queue.append(temp)

        # remove the first node from the queue
        del queue[0]

    # if reach this point, then the answer must be unsuccess
    return answer