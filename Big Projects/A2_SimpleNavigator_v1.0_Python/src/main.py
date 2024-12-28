from my_graph import Graph
from my_graph_algorithms import GraphAlgorithms
from sys import exit


def print_menu():
    print()
    print("-----------------------------------------------------------")
    print("Enter the number of algorithm you want to use on the graph:")
    print("1 - Depth first search")
    print("2 - Breadth first search")
    print("3 - Find the shortest path between ", end='')
    print("any two vertices (Dijkstra's algorithm)")
    print("4 - Find the shortest paths between ", end='')
    print("all pairs of vertices in the graph (Floyd-Warshall algorithm)")
    print("5 - Search for the minimum spanning tree ", end='')
    print("in the graph (Prim's algorithm)")
    print("6 - Traveling salesman problem (Ant colony algorithm)")
    print("0 - If you want to exit")


def menu_input_handler():
    success = False
    while not success:
        try:
            input_alg = int(input())
            if input_alg == 0:
                exit(0)
            elif input_alg >= 1 and input_alg <= 6:
                success = True
            else:
                print("Enter the algorithm number from 1 to 6 or 0 to exit:")
        except Exception as exp:
            print("Enter the algorithm number from 1 to 6 or 0 to exit:")
    return input_alg


def vertex_input_handler(message):
    if message:
        print(message)
    success = False
    while not success:
        try:
            input_vertex = int(input())
            success = True
            return input_vertex
        except Exception as exp:
            print("Error. " + message)


def command_line_interface():
    print("Hi, it is a console application for testing ", end='')
    print("the functionality of the graph algorithms.")
    success = False
    g = Graph()
    g_algs = GraphAlgorithms()

    while not success:
        print("To load the  graph from a file in the adjacency matrix, ", end='')
        print("format enter it's filename:")
        filename = str(input())
        success = g.load_graph_from_file(filename)
        if not success:
            print("Filename is incorrect, try again or exit:")

    while 1:
        print_menu()
        input_alg = menu_input_handler()
        try:
            match input_alg:
                case 1:
                    v = vertex_input_handler("Enter the start vertex number:")
                    res = g_algs.depth_first_search(g, v)
                    print("The vertices in the order they were traversed:")
                    print(res)
                case 2:
                    v = vertex_input_handler("Enter the start vertex number:")
                    res = g_algs.breadth_first_search(g, v)
                    print("The vertices in the order they were traversed:")
                    print(res)
                case 3:
                    v1 = vertex_input_handler("Enter the start vertex number:")
                    v2 = vertex_input_handler("Enter the finish vertex ")
                    res = g_algs.get_shortest_path_between_vertices(g, v1, v2)
                    print("The smallest distance between ", end='')
                    print(f"vertices {v1} and {v2} is: ")
                    print("res", res)
                case 4:
                    res = g_algs.get_shortest_paths_between_all_vertices(g)
                    print("The matrix of the shortest paths between ", end='')
                    print("all vertices of the graph is:")
                    for row in res:
                        print(row)
                case 5:
                    res = g_algs.get_least_spanning_tree(g)
                    print("The adjacency matrix for the ", end='')
                    print("minimal spanning tree is:")
                    for row in res:
                        print(row)
                case 6:
                    res = g_algs.solve_traveling_salesman_problem(g)
                    print("Traveling salesman problem answer:")
                    print("1 - the shortest path that goes through all vertices: ", end='')
                    print([res.vertices[i] for i in range(len(g.get_graph_matrix()) + 1)])
                    print("2 - the length of this route = ", res.distance)
        except Exception as exp:
            print(exp)


if __name__ == "__main__":
    command_line_interface()
