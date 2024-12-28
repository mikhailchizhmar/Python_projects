import random


class CaveGenerator:
    def __init__(self, rows, cols, birth_limit, death_limit, initial_fill_prob):
        self.rows = rows
        self.cols = cols
        self.birth_limit = birth_limit
        self.death_limit = death_limit
        self.initial_fill_prob = initial_fill_prob
        self.grid = self.initialize_grid()

    def initialize_grid(self):
        grid = []
        for i in range(self.rows):
            grid.append([1 if random.random() < self.initial_fill_prob else 0 for _ in range(self.cols)])
        return grid

    def count_alive_neighbors(self, grid, x, y):
        alive = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if i == x and j == y:
                    continue
                if i < 0 or j < 0 or i >= self.rows or j >= self.cols:
                    alive += 1
                elif grid[i][j] == 1:
                    alive += 1
        return alive

    def simulate_step(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for i in range(self.rows):
            for j in range(self.cols):
                alive_neighbors = self.count_alive_neighbors(self.grid, i, j)
                if self.grid[i][j] == 1:
                    if alive_neighbors < self.death_limit:
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] = 1
                else:
                    if alive_neighbors > self.birth_limit:
                        new_grid[i][j] = 1
                    else:
                        new_grid[i][j] = 0
        self.grid = new_grid

    def load_from_file(self, file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            self.rows, self.cols = map(int, lines[0].split())
            self.grid = []
            for i in range(1, self.rows + 1):
                self.grid.append(list(map(int, lines[i].split())))

    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            f.write(f"{self.rows} {self.cols}\n")
            for row in self.grid:
                f.write(" ".join(map(str, row)) + "\n")
