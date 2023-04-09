import pyfiglet 
from lib.util import *

def print_welcome_screen():
    welcome_text = pyfiglet.figlet_format("Path Finder App")
    print(welcome_text)
    print()
    print('#' * 70)
    print()

def print_exit_screen():
    print()
    print("#" * 70)
    print()
    exit_text = pyfiglet.figlet_format("THANK YOU!")
    print(exit_text)
    print()

def ask_algorithm():
    print("Pilih algoritma yang ingin digunakan")
    print("""
   ##########################
    1. Uniform Cost Search
    2. A* 
    """)
    correct_input = False

    while(not correct_input):
        try:
            action = input("Pilihan(1-3): ")
            correct_input = (0 < int(action) < 4)
        except:
            print("Input tidak valid!")
    
    return action

def create_graph_from_input_file():
    correct_input = False
    while(not correct_input):
        try:
            file_name = input("Masukkan nama file: ")
            graph = read_graph_from_file(file_name)
            print("Graph berhasil dibaca dari file input.")
            correct_input = True
        except:
            print("File tidak ditemukan!")
    
    return graph

def ask_start_node(graph: Graph):
    start = input("Masukkan nama titik asal: ")
    start_node_index = get_node_idx_from_name(start, graph)
    while(start_node_index == -1):
        print("Titik awal tidak ditemukan, tolong masukkan input yang benar!")
        start = input("Silahkan ulangi input nama titik asal: ")
        start_node_index = get_node_idx_from_name(start, graph)
    
    return start_node_index

def ask_goal_node(graph: Graph):
    goal = input("Masukkan nama titik tujuan: ")
    goal_node_index = get_node_idx_from_name(goal, graph)
    while(goal_node_index == -1):
        print("Titik awal tidak ditemukan, tolong masukkan input yang benar!")
        goal = input("Silahkan ulangi input nama titik tujuan: ")
        goal_node_index = get_node_idx_from_name(goal, graph)
    
    return goal_node_index

def print_answer(answer: dict):
    if(answer["success"]):
        for node in answer["path"]:
            print(node.name())
        print(answer["cost"])
    else:
        print("Fail bang")

def continue_or_not():
    print()
    print('#' * 70)
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