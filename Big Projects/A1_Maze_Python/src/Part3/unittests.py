import unittest
from MazeSolver import MazeSolver


class TestMazeSolver(unittest.TestCase):
    def test_solver_simple_maze(self):
        vertical_walls = [
            [0, 0, 1],
            [1, 1, 1],
            [1, 0, 1]
        ]
        horizontal_walls = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        solver = MazeSolver(vertical_walls, horizontal_walls)
        path = solver.solve_maze((0, 0), (2, 2))
        expected_path = [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]
        self.assertEqual(path, expected_path)

    def test_no_solution(self):
        vertical_walls = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        horizontal_walls = [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ]
        solver = MazeSolver(vertical_walls, horizontal_walls)
        path = solver.solve_maze((0, 0), (2, 2))
        self.assertIsNone(path)

    def test_invalid_points(self):
        vertical_walls = [
            [1, 0, 1],
            [1, 0, 1],
            [1, 0, 1]
        ]
        horizontal_walls = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        solver = MazeSolver(vertical_walls, horizontal_walls)
        with self.assertRaises(ValueError):
            solver.solve_maze((-1, 0), (2, 2))
        with self.assertRaises(ValueError):
            solver.solve_maze((0, 0), (3, 2))


if __name__ == "__main__":
    unittest.main()
