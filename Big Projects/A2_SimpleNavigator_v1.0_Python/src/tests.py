import unittest
from my_graph import Graph
from my_graph_algorithms import GraphAlgorithms


class TestSimpleNavigator(unittest.TestCase):
    def test_depth_first_search_1(self):
        x = Graph()
        x.load_graph_from_file('data/graphBFS1.txt')
        z = GraphAlgorithms()
        res = z.depth_first_search(x, 2)
        answer = [2, 5, 1, 3, 4, 6]
        x.export_graph_to_dot("1.dot")
        self.assertEqual(res, answer)

    def test_depth_first_search_2(self):
        x = Graph()
        x.load_graph_from_file('data/graphBFS2.txt')
        z = GraphAlgorithms()
        res = z.depth_first_search(x, 5)
        answer = [5, 3, 1, 2, 4, 7, 9, 6, 10, 8]
        self.assertEqual(res, answer)

    def test_depth_first_search_3(self):
        x = Graph()
        x.load_graph_from_file('data/graphDij2.txt')
        z = GraphAlgorithms()
        res = z.depth_first_search(x, 3)
        answer = [3, 1, 2, 4, 5, 6]
        self.assertEqual(res, answer)

    def test_depth_first_search_4(self):
        x = Graph()
        x.load_graph_from_file('data/graphDij2.txt')
        z = GraphAlgorithms()
        res = z.depth_first_search(x, 6)
        answer = [6, 1, 2, 3, 4, 5]
        self.assertEqual(res, answer)

    def test_depth_first_search_5(self):
        x = Graph()
        x.load_graph_from_file('data/graphDij.txt')
        z = GraphAlgorithms()
        res = z.depth_first_search(x, 2)
        answer = [2, 1, 3, 5, 4, 7, 6]
        self.assertEqual(res, answer)

    def test_depth_first_search_6(self):
        x = Graph()
        x.load_graph_from_file('data/graphDij.txt')
        z = GraphAlgorithms()
        res = z.depth_first_search(x, 7)
        answer = [7, 4, 2, 1, 3, 5, 6]
        self.assertEqual(res, answer)

    def test_breadth_first_search_1(self):
        x = Graph()
        x.load_graph_from_file('data/graphBFS1.txt')
        z = GraphAlgorithms()
        res = z.breadth_first_search(x, 2)
        answer = [2, 5, 6, 1, 4, 3]
        self.assertEqual(res, answer)

    def test_breadth_first_search_2(self):
        x = Graph()
        x.load_graph_from_file('data/graph0.txt')
        z = GraphAlgorithms()
        res = z.breadth_first_search(x, 3)
        answer = [3, 1, 2, 4]
        self.assertEqual(res, answer)

    def test_breadth_first_search_3(self):
        x = Graph()
        x.load_graph_from_file('data/graphBFS1.txt')
        z = GraphAlgorithms()
        res = z.breadth_first_search(x, 6)
        answer = [6, 2, 3, 5, 1, 4]
        self.assertEqual(res, answer)

    def test_breadth_first_search_4(self):
        x = Graph()
        x.load_graph_from_file('data/graphBFS2.txt')
        z = GraphAlgorithms()
        res = z.breadth_first_search(x, 3)
        answer = [3, 1, 2, 4, 5, 8, 9, 10, 7, 6]
        self.assertEqual(res, answer)

    def test_breadth_first_search_5(self):
        x = Graph()
        x.load_graph_from_file('data/graphBFS2.txt')
        z = GraphAlgorithms()
        res = z.breadth_first_search(x, 7)
        answer = [7, 1, 2, 4, 9, 10, 3, 8, 6, 5]
        self.assertEqual(res, answer)

    def test_get_shortest_path_between_vertices_1(self):
        x = Graph()
        filename = "data/graph3.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_shortest_path_between_vertices(x, 1, 5)
        self.assertEqual(res, 6)

    def test_get_shortest_path_between_vertices_2(self):
        x = Graph()
        filename = "data/graphDij2.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_shortest_path_between_vertices(x, 2, 6)
        self.assertEqual(res, 12)

    def test_get_shortest_path_between_vertices_3(self):
        x = Graph()
        filename = "data/graphDij.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_shortest_path_between_vertices(x, 1, 7)
        self.assertEqual(res, 13)

    def test_get_shortest_path_between_vertices_4(self):
        x = Graph()
        filename = "data/graph1.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_shortest_path_between_vertices(x, 4, 11)
        self.assertEqual(res, 25)

    def test_get_shortest_path_between_vertices_5(self):
        x = Graph()
        filename = "data/graphDij.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        with self.assertRaises(ValueError):
            res = z.get_shortest_path_between_vertices(x, 8, 1)

    def test_get_shortest_paths_between_all_vertices_1(self):
        x = Graph()
        filename = "data/graphDij.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_shortest_paths_between_all_vertices(x)
        answer = [[ 0,  5,  8, 10, 11, 13, 13],
                  [ 5,  0,  3,  5,  6,  8,  8],
                  [ 8,  3,  0,  5,  4,  6,  7],
                  [10,  5,  5,  0,  1,  3,  3],
                  [11,  6,  4,  1,  0,  2,  3],
                  [13,  8,  6,  3,  2,  0,  1],
                  [13,  8,  7,  3,  3,  1,  0]]
        self.assertEqual(res, answer)

    def test_get_shortest_paths_between_all_vertices_2(self):
        x = Graph()
        filename = "data/graphDij2.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_shortest_paths_between_all_vertices(x)
        answer = [[ 0,  7,  9, 20, 20, 11],
                  [ 7,  0, 10, 15, 21, 12],
                  [ 9, 10,  0, 11, 11,  2],
                  [20, 15, 11,  0,  6, 13],
                  [20, 21, 11,  6,  0,  9],
                  [11, 12,  2, 13,  9,  0]]
        self.assertEqual(res, answer)

    def test_get_least_spanning_tree(self):
        x = Graph()
        filename = "data/graph0.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_least_spanning_tree(x)
        answer = [[0, 1, 2, 0], 
                  [1, 0, 0, 5],
                  [2, 0, 0, 0],
                  [0, 5, 0, 0]]
        self.assertEqual(res, answer)

    def test_get_least_spanning_tree2(self):
        x = Graph()
        filename = "data/graphP1.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_least_spanning_tree(x)
        answer = [[0, 2, 3, 3, 0, 0, 0], 
                  [2, 0, 0, 0, 0, 0, 0],
                  [3, 0, 0, 0, 1, 6, 0],
                  [3, 0, 0, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0, 0],
                  [0, 0, 6, 0, 0, 0, 9],
                  [0, 0, 0, 0, 0, 9, 0]]
        self.assertEqual(res, answer)
    
    def test_get_least_spanning_tree3(self):
        x = Graph()
        filename = "data/graphP2.txt"
        x.load_graph_from_file(filename)
        z = GraphAlgorithms()
        res = z.get_least_spanning_tree(x)
        answer = [[0, 5, 0, 0, 0, 0, 1], 
                  [5, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 4],
                  [0, 0, 0, 0, 4, 0, 0],
                  [0, 0, 0, 4, 0, 0, 3],
                  [0, 0, 0, 0, 0, 0, 8],
                  [1, 0, 4, 0, 3, 8, 0]]
        self.assertEqual(res, answer)

    def test_solve_traveling_salesman_problem_1(self):
        x = Graph()
        x.load_graph_from_file('data/graphS1.txt')
        z = GraphAlgorithms()
        result = z.solve_traveling_salesman_problem(x)
        distance = result.distance
        vertices = [result.vertices[i] for i in range(len(x.get_graph_matrix()) + 1)]
        expected_path = [1, 2, 3, 4, 1]
        expected_length = 4
        self.assertEqual(vertices, expected_path)
        self.assertEqual(distance, expected_length)

    def test_solve_traveling_salesman_problem_2(self):
        x = Graph()
        x.load_graph_from_file('data/graph8.txt')
        z = GraphAlgorithms()
        result = z.solve_traveling_salesman_problem(x)
        distance = result.distance
        vertices = [result.vertices[i] for i in range(len(x.get_graph_matrix()) + 1)]
        expected_path = [1, 4, 3, 6, 5, 2, 1]
        expected_length = 85
        self.assertEqual(vertices, expected_path)
        self.assertEqual(distance, expected_length)


if __name__ == "__main__":
    unittest.main()
