import unittest
import os
from MazeEller import MazeGenerator  # Ensure the MazeGenerator class is imported correctly


class TestMazeGenerator(unittest.TestCase):
    def setUp(self):
        self.maze = MazeGenerator(4, 4)

    def test_initialization(self):
        self.assertEqual(self.maze.rows, 4)
        self.assertEqual(self.maze.cols, 4)
        for row in self.maze.vertical_walls:
            self.assertEqual(row, [1, 1, 1, 1])
        for row in self.maze.horizontal_walls:
            self.assertEqual(row, [1, 1, 1, 1])

    def test_generate_maze(self):
        self.maze.generate_maze()
        visited = set()
        self.dfs_check((0, 0), visited)
        self.assertEqual(len(visited), self.maze.rows * self.maze.cols)

    def dfs_check(self, cell, visited):
        row, col = cell
        if cell in visited:
            return
        visited.add(cell)
        neighbors = self.maze.get_unvisited_neighbors(row, col, visited)
        for neighbor in neighbors:
            if not self.is_wall_between(cell, neighbor):
                self.dfs_check(neighbor, visited)

    def is_wall_between(self, cell1, cell2):
        row1, col1 = cell1
        row2, col2 = cell2
        if row1 == row2:
            if col1 < col2:
                return self.maze.vertical_walls[row1][col1] == 1
            else:
                return self.maze.vertical_walls[row1][col2] == 1
        elif col1 == col2:
            if row1 < row2:
                return self.maze.horizontal_walls[row1][col1] == 1
            else:
                return self.maze.horizontal_walls[row2][col1] == 1
        return True

    def test_remove_wall(self):
        # Test removing walls between adjacent cells
        self.maze.remove_wall((0, 0), (0, 1))
        self.assertEqual(self.maze.vertical_walls[0][0], 0)

        self.maze.remove_wall((1, 0), (0, 0))
        self.assertEqual(self.maze.horizontal_walls[0][0], 0)

    def test_load_from_file(self):
        test_data = "4 4\n0 1 0 1\n1 0 1 1\n0 1 0 1\n1 1 1 0\n\n1 0 1 0\n0 1 0 1\n1 1 0 1\n1 0 1 1\n"
        test_file = "test_maze.txt"
        with open(test_file, 'w') as f:
            f.write(test_data)

        self.maze.load_from_file(test_file)
        self.assertEqual(self.maze.rows, 4)
        self.assertEqual(self.maze.cols, 4)
        self.assertEqual(self.maze.vertical_walls, [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]])
        self.assertEqual(self.maze.horizontal_walls, [[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1]])

        os.remove(test_file)

    def test_save_to_file(self):
        self.maze.vertical_walls = [[0, 1, 0, 1], [1, 0, 1, 1], [0, 1, 0, 1], [1, 1, 1, 0]]
        self.maze.horizontal_walls = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [1, 0, 1, 1]]
        test_file = "test_save_maze.txt"
        self.maze.save_to_file(test_file)

        with open(test_file, 'r') as f:
            content = f.read()

        expected_content = "4 4\n0 1 0 1\n1 0 1 1\n0 1 0 1\n1 1 1 0\n\n1 0 1 0\n0 1 0 1\n1 1 0 1\n1 0 1 1\n"
        self.assertEqual(content, expected_content)

        os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
