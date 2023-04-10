from lib.util import *
from lib.ucs import *
from lib.astar import *
from lib.IO import *

def start_program():
    print_welcome_screen()
    keep_playing = True

    while(keep_playing):    
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
        cont = continue_or_not()
        keep_playing = False
        if(cont):
            keep_playing = True
            change_the_map = change_map()
            while(not change_the_map):
                print("#" * 70)
                print()
                start_index = ask_start_node(graph)
                goal_index = ask_goal_node(graph)
                
                choice = ask_algorithm()
                if(choice == 1):
                    ans = ucs(graph.nodes()[start_index], graph.nodes()[goal_index], graph)
                else:
                    ans = astar(graph.nodes()[start_index], graph.nodes()[goal_index], graph)
                print()
                print_answer(ans)

                cont = continue_or_not()
                if(cont):
                    change_the_map = change_map()
                else:
                    change_the_map = False
                    keep_playing = False
        
    print_exit_screen()

if __name__ == '__main__':
    start_program()