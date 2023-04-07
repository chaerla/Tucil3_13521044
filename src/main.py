from lib.util import *
from lib.ucs import *

graph = read_graph_from_file("Alun Alun Kota Bandung")
graph.show()

ans = ucs(graph.nodes()[0], graph.nodes()[len(graph.adjmatrix())-1], graph)
for node in ans["path"]:
    print(node.name())
print(ans["cost"])