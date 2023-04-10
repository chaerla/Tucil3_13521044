from main import *
from flask import Flask
import folium
from folium.plugins import MarkerCluster
from folium.vector_layers import PolyLine

app = Flask(__name__)
result = None

@app.route('/')
def index():
    graph = result["graph"]
    path = result["path"]
    # Create the map
    m = folium.Map(location=[graph.nodes()[0].latitude(), graph.nodes()[0].longitude()], zoom_start=16)

    # Add markers to the map
    marker_cluster = MarkerCluster().add_to(m)
    for node in graph.nodes():
        folium.Marker(location=[node.latitude(), node.longitude()], popup=str(node.index() + 1)).add_to(marker_cluster)
    # Add polylines to the map based on the adjacency matrix
    for i in range(len(graph.adjmatrix())):
        for j in range(i+1, len(graph.adjmatrix()[i])):
            if graph.adjmatrix()[i][j] != -1:
                line = PolyLine(locations=[[graph.nodes()[i].latitude(), graph.nodes()[i].longitude()], (graph.nodes()[j].latitude(), graph.nodes()[j].longitude())], color='red', weight=5, opacity=0.7).add_to(m)
    # Add polylines to the map based on the result path
    for i in range(len(path)-1):
        line = PolyLine(locations=[[path[i].latitude(), path[i].longitude()], (path[i+1].latitude(), path[i+1].longitude())], color='green', weight=5, opacity=0.7).add_to(m)
    # Return the map
    return m._repr_html_()

if __name__ == '__main__':
    print_welcome_screen()
    graph = create_graph_from_input_file()
    start_index = ask_start_node(graph)
    goal_index = ask_goal_node(graph)
    
    choice = ask_algorithm()
    if(choice == 1):
        ans = ucs(graph.nodes()[start_index], graph.nodes()[goal_index], graph)
    else:
        ans = astar(graph.nodes()[start_index], graph.nodes()[goal_index], graph)
    
    print()
    print_answer(ans)
    print("Map hasil visualisasi graf dapat dilihat pada localhost:5000")
    ans["graph"] = graph
    result = ans
    app.run(debug=False)