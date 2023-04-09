from lib.util import *
from lib.ucs import *
from lib.astar import *

graph = read_graph_from_file("Alun Alun Kota Bandung")
# graph.show()

print()
ans = ucs(graph.nodes()[6], graph.nodes()[len(graph.adjmatrix())-1], graph)
if(ans["success"]):
    for node in ans["path"]:
        print(node.name())
    print(ans["cost"])
else:
    print("Fail bang")

print()

ans2 = astar(graph.nodes()[6], graph.nodes()[len(graph.adjmatrix())-1], graph)
if(ans2["success"]):
    for node in ans2["path"]:
        print(node.name())
    print(ans2["cost"])
else:
    print("Fail bang")
