from help import Stack, Queue, Ant, correct_path
import ctypes
import random
import numpy as np


class TsmResult(ctypes.Structure):
    _fields_ = [("vertices", ctypes.POINTER(ctypes.c_int)), ("distance", ctypes.c_double)]


class GraphAlgorithms:
    @staticmethod
    def depth_first_search(graph, start_vertex):
        matrix = graph.get_graph_matrix().copy()
        stack = Stack()
        stack.push(start_vertex)
        visited = []

        while not stack.empty():
            v = stack.pop()
            if v not in visited:
                visited.append(v)
                for i in range(len(matrix) - 1, -1, -1):
                    if matrix[v - 1][i] and i + 1 not in visited:
                        stack.push(i + 1)

        return visited

    @staticmethod
    def breadth_first_search(graph, start_vertex):
        matrix = graph.get_graph_matrix().copy()
        queue = Queue()
        queue.push(start_vertex)
        visited = []

        while not queue.empty():
            v = queue.pop()
            if v not in visited:
                visited.append(v)
                for i in range(0, len(matrix)):
                    if matrix[v - 1][i] and i + 1 not in visited:
                        queue.push(i + 1)

        return visited

    @staticmethod
    def get_shortest_path_between_vertices(graph, vertex1, vertex2):
        matrix = graph.get_graph_matrix().copy()
        valid = [i for i in range(1, len(matrix) + 1)]
        if vertex1 not in valid or vertex2 not in valid:
            raise ValueError("Incorrect input")

        shortest_paths = {k: float("inf") for k in range(1, len(matrix) + 1)}
        unvisited = [i for i in range(1, len(matrix) + 1)]
        shortest_paths[vertex1] = 0

        while unvisited:
            min_node = None

            for node in unvisited:
                if min_node is None:
                    min_node = node
                elif shortest_paths[node] < shortest_paths[min_node]:
                    min_node = node

            for j in range(0, len(matrix)):
                cost = matrix[min_node - 1][j]
                to_node = j + 1
                if not cost:
                    continue
                if cost + shortest_paths[min_node] < shortest_paths[to_node]:
                    shortest_paths[to_node] = cost + shortest_paths[min_node]

            unvisited.remove(min_node)
        return shortest_paths[vertex2]

    @staticmethod
    def get_shortest_paths_between_all_vertices(graph):
        matrix_in = graph.get_graph_matrix().copy()
        size = len(matrix_in)

        matrix_out = [[float("inf")] * size for _ in range(size)]
        for i in range(size):
            matrix_out[i][i] = 0

        for i in range(size):
            for j in range(size):
                if matrix_in[i][j] != 0:
                    matrix_out[i][j] = int(matrix_in[i][j])

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if matrix_out[i][j] > matrix_out[i][k] + matrix_out[k][j]:
                        matrix_out[i][j] = int(matrix_out[i][k] + matrix_out[k][j])

        return matrix_out

    @staticmethod
    def get_least_spanning_tree(graph):
        if not graph.is_directed_graph():
            return "Error. Only connected undirected graph"

        matrix_in = graph.get_graph_matrix().copy()
        size = len(matrix_in)
        matrix_out = [[0] * size for _ in range(size)]

        unvisited = [i for i in range(size)]
        visited = [unvisited[0]]
        unvisited.remove(unvisited[0])

        while unvisited:
            edges_from_visited_node = [int(matrix_in[node][i]) if i in unvisited and matrix_in[node][i] != 0
                                       else float("inf") for node in visited for i in range(size)]
            current_min_weight = min(edges_from_visited_node)

            break_out_flag = False
            for node_from in visited:
                for i in range(size):
                    if matrix_in[node_from][i] == current_min_weight and i in unvisited:
                        visited.append(i)
                        unvisited.remove(i)
                        matrix_out[node_from][i] = int(current_min_weight)
                        matrix_out[i][node_from] = int(current_min_weight)
                        break_out_flag = True
                        break
                if break_out_flag:
                    break
        return matrix_out

    @staticmethod
    def solve_traveling_salesman_problem(graph):
        matrix = graph.get_graph_matrix().copy()
        if len([num for row in matrix for num in row if num == 0]) == len(matrix):
            alfa = 1
            betta = 4
            evaporation = 0.6
            q = 40
            count = 1000
            pheromones = np.array([[0.1 for _ in range(len(matrix))] for _ in range(len(matrix))])
            min_path_length = float('inf')
            min_path = []
            for _ in range(count):
                pheromones *= evaporation
                for _ in range(len(pheromones)):  # amount of ants
                    start_position = random.randint(0, graph.get_graph_size() - 1)
                    ant = Ant(start_position, alfa, betta)
                    tmp_length = ant.make_path(graph.get_graph_matrix(), pheromones)
                    if min_path_length > tmp_length:
                        min_path_length = tmp_length
                        min_path = ant.path
                    for i in range(len(ant.path) - 1):
                        pheromones[ant.path[i]][ant.path[i + 1]] += q / ant.path_length
            min_path = [i + 1 for i in min_path]
            min_path = correct_path(min_path)
            path_array = (ctypes.c_int * len(min_path))(*min_path)
            return TsmResult(vertices=path_array, distance=min_path_length)
        else:
            raise ValueError('Invalid graph!')
