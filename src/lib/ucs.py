from lib.graph import *
from lib.node import *

def ucs(start: Node, goal: Node, graph: Graph):
    """
    A function to find the shortest path between start and goal
    returns a dictionary:
    {
        "cost" : {the cost of the path}
        "path" : {the shortest path between the nodes}
        "success" : {whether or not there's a path connecting the start and goal}
    }
    """

    queue = [] #priority queue that stores the nodes to be visited

    # the queue element has node(the node to be visited), cost(the cost to visit the node), path(the path to reach the node)
    queue.append({
        "node": start,
        "cost": 0,
        "path": [start]
    })

    # initialize the answer to the starting node
    answer = {
        "cost": start,
        "path": 0,
        "success": False,
    }

    # list to store the index of the visited nodes
    visited = []
    while (len(queue) > 0):
        queue = sorted(queue, key=lambda x: x["cost"])

        # the current node to check
        curr = {
            "node": queue[0]["node"],
            "cost": queue[0]["cost"],
            "path": queue[0]["path"]
        }

        # checks if it hasnt been visited yet
        if (curr["node"].index() not in visited):
            # if the current node is the goal, return
            if (curr["node"].index() == goal.index()):
                answer = {
                        "cost": curr["cost"],
                        "path": curr["path"],
                        "success": True,
                    }
                return answer
            # expands the node, push all its neighbours to the priority queue
            for i in range (len(graph.adjmatrix()[curr["node"].index()])):
                if(graph.adjmatrix()[curr["node"].index()][i]!=-1):
                    temp = {
                        "node": graph.nodes()[i],
                        "cost": curr["cost"] + graph.adjmatrix()[curr["node"].index()][i],
                        "path": curr["path"] + [graph.nodes()[i]]
                    }
                    queue.append(temp)
            queue = sorted(queue, key=lambda x: x["cost"])

            # add the node to the visited list
            visited.append(curr["node"].index())
        
        # pop the node from the queue
        del queue[0]

    return answer
                




