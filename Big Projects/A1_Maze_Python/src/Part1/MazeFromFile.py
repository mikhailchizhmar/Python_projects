import random


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.vertical_walls = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.horizontal_walls = [[1 for _ in range(self.cols)] for _ in range(self.rows)]

    def load_from_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.rows, self.cols = map(int, lines[0].split())
            self.vertical_walls = []
            self.horizontal_walls = []

            for i in range(1, self.rows + 1):
                self.vertical_walls.append(list(map(int, lines[i].split())))

            for i in range(self.rows + 2, 2 * self.rows + 2):
                self.horizontal_walls.append(list(map(int, lines[i].split())))


