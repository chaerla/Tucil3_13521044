import pyfiglet 
from lib.util import *

def print_welcome_screen():
    """
    prints splash screen
    """
    welcome_text = pyfiglet.figlet_format("Path Finder App")
    print(welcome_text)
    print()
    print('#' * 75)
    print()

def print_exit_screen():
    """
    prints exit splash screen
    """
    print()
    print("#" * 70)
    print()
    exit_text = pyfiglet.figlet_format("THANK YOU!")
    print(exit_text)
    print()

def ask_algorithm():
    """
    asks for algorithm choice
    """
    print("Pilih algoritma yang ingin digunakan")
    print("""
    ##########################
    1. Uniform Cost Search
    2. A* 
    ##########################
    """)
    correct_input = False

    while(not correct_input):
        try:
            action = input("Pilihan(1-2): ")
            correct_input = (0 < int(action) < 3)
        except:
            print("Input tidak valid!")
    
    return int(action)

def create_graph_from_input_file():
    correct_input = False
    while(not correct_input):
        try:
            file_name = input("Masukkan nama file (dalam folder test): ")
            print(file_name)
            graph = read_graph_from_file(file_name)
            print("Graph berhasil dibaca dari file input.")
            correct_input = True
        except:
            print("Terjadi kesalahan saat membaca file! Pastikan anda memasukkan file yang benar")
    
    return graph

def ask_start_node(graph: Graph):
    graph.show()
    print()
    start = (input(f"Pilih titik asal [1-{len(graph.nodes())}]: "))
    print()
    # start_node_index = get_node_idx_from_name(start, graph)
    try:
        start = int(start)
    except ValueError:
        print("Titik awal harus berupa bilangan bulat!")
        return ask_start_node(graph)
    
    if(start<1 or start > len(graph.nodes())):
        print("Titik awal tidak ditemukan, tolong masukkan input yang benar!")
        return ask_start_node(graph)

    return start-1

def ask_goal_node(graph: Graph):
    # graph.show()
    # print()
    goal = (input(f"Pilih titik tujuan [1-{len(graph.nodes())}]: "))
    print()
    try:
        goal = int(goal)
    except ValueError:
        print("Pilihan harus berupa bilangan bulat!")
        return ask_goal_node(graph)
    
    # goal_node_index = get_node_idx_from_name(goal, graph)
    if(goal<1 or goal > len(graph.nodes())):
        print("Titik awal tidak ditemukan, tolong masukkan input yang benar!")
        return ask_goal_node(graph)
        
    return goal-1

def print_answer(answer: dict):
    print("#"*70)
    print()
    if(answer["success"]):
        print("Lintasan   :     ",end="")
        for i in range (len(answer["path"])):
            if(i!=len(answer["path"])-1):
                print(answer["path"][i].name(), end=" - ")
            else:
                print(answer["path"][i].name())
        print("Jarak(km)  :     " + str(answer["cost"]))
    else:
        print("Tidak ada lintasan yang ditemukan!")
    print()
    print("#"*70)

def continue_or_not():
    print()
    print()
    answer = False
    ask = input("Ingin mencari titik lain? [y/n]: ").lower()
    if(ask == 'y'):
        answer = True
        print()
        # print("#" * 70)
        # print()
    
    return answer

def change_map():
    answer = False
    ask = input("Ingin mengganti map? [y/n]: ").lower()
    if(ask == 'y'):
        answer = True
        print()
        print("#" * 70)
        print()
    
    return answer