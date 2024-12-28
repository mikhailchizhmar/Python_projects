import unittest
from MazeCaveGenerator import CaveGenerator


class TestCaveGenerator(unittest.TestCase):
    def test_initial_grid(self):
        generator = CaveGenerator(10, 10, 4, 3, 0.4)
        self.assertEqual(len(generator.grid), 10)
        self.assertEqual(len(generator.grid[0]), 10)

    def test_alive_neighbors(self):
        grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        generator = CaveGenerator(3, 3, 4, 3, 0.4)
        generator.grid = grid
        self.assertEqual(generator.count_alive_neighbors(grid, 1, 1), 8)
        self.assertEqual(generator.count_alive_neighbors(grid, 0, 0), 7)

    def test_simulate_step(self):
        generator = CaveGenerator(3, 3, 4, 3, 0.4)
        generator.grid = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        generator.simulate_step()
        self.assertEqual(generator.grid, [
            [1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]
        ])

    def test_load_from_file(self):
        with open('test_cave.txt', 'w') as f:
            f.write("3 3\n")
            f.write("1 0 1\n")
            f.write("0 1 0\n")
            f.write("1 0 1\n")

        generator = CaveGenerator(1, 1, 0, 0, 0)
        generator.load_from_file('test_cave.txt')
        self.assertEqual(generator.rows, 3)
        self.assertEqual(generator.cols, 3)
        self.assertEqual(generator.grid, [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ])

    def test_save_to_file(self):
        generator = CaveGenerator(3, 3, 4, 3, 0.4)
        generator.grid = [
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ]
        generator.save_to_file('output_cave.txt')
        with open('output_cave.txt', 'r') as f:
            lines = f.readlines()
        self.assertEqual(lines, [
            "3 3\n",
            "1 0 1\n",
            "0 1 0\n",
            "1 0 1\n"
        ])


if __name__ == "__main__":
    unittest.main()
