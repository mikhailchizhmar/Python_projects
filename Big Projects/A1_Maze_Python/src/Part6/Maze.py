import random

from PIL import Image, ImageDraw


class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.vertical_walls = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.horizontal_walls = [[1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.solution_path = []

    def save_to_file_(self, file_path, data):
        with open(file_path, 'w') as f:
            f.write(data)

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

    def generate_maze(self):

        stack = [(0, 0)]
        visited = set(stack)

        while stack:
            current_cell = stack[-1]
            row, col = current_cell
            neighbors = self.get_unvisited_neighbors(row, col, visited)

            if neighbors:
                chosen = random.choice(neighbors)
                stack.append(chosen)
                self.remove_wall(current_cell, chosen)
                visited.add(chosen)
            else:
                stack.pop()

    def get_unvisited_neighbors(self, row, col, visited):
        neighbors = []

        if row > 0 and (row - 1, col) not in visited:
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and (row + 1, col) not in visited:
            neighbors.append((row + 1, col))
        if col > 0 and (row, col - 1) not in visited:
            neighbors.append((row, col - 1))
        if col < self.cols - 1 and (row, col + 1) not in visited:
            neighbors.append((row, col + 1))

        return neighbors

    def remove_wall(self, cell1, cell2):
        row1, col1 = cell1
        row2, col2 = cell2

        if row1 == row2:
            if col1 < col2:
                self.vertical_walls[row1][col1] = 0
            else:
                self.vertical_walls[row1][col2] = 0
        elif col1 == col2:
            if row1 < row2:
                self.horizontal_walls[row1][col1] = 0
            else:
                self.horizontal_walls[row2][col1] = 0

    def save_to_file(self, file_path):
        with open(file_path, 'w') as f:
            f.write(f"{self.rows} {self.cols}\n")
            for row in self.vertical_walls:
                f.write(" ".join(map(str, row)) + "\n")
            f.write("\n")
            for row in self.horizontal_walls:
                f.write(" ".join(map(str, row)) + "\n")

    def solve_maze(self, start, end):
        # Validate points
        if not self.is_valid_point(start) or not self.is_valid_point(end):
            raise ValueError("Start or end point is out of maze bounds.")

        self.solution_path = []
        self.visited = set()
        if self._dfs(start, end):
            self.solution_path.reverse()
            return self.solution_path
        return None

    def is_valid_point(self, point):
        row, col = point
        return 0 <= row < self.rows and 0 <= col < self.cols

    def _dfs(self, current, end):
        if current == end:
            self.solution_path.append(current)
            return True

        row, col = current
        self.visited.add(current)

        neighbors = self.get_neighbors(row, col)
        for neighbor in neighbors:
            if neighbor not in self.visited:
                if self._dfs(neighbor, end):
                    self.solution_path.append(current)
                    return True

        return False

    def get_neighbors(self, row, col):
        neighbors = []
        if row > 0 and not self.horizontal_walls[row - 1][col]:  # Up
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and not self.horizontal_walls[row][col]:  # Down
            neighbors.append((row + 1, col))
        if col > 0 and not self.vertical_walls[row][col - 1]:  # Left
            neighbors.append((row, col - 1))
        if col < self.cols - 1 and not self.vertical_walls[row][col]:  # Right
            neighbors.append((row, col + 1))

        return neighbors

    def draw(self, with_solution: bool = False):

        cell_size = min(500 // self.rows, 500 // self.cols)
        margin = 10

        image1 = Image.new("RGB", (520, 520), "black")
        draw = ImageDraw.Draw(image1)
        draw.rectangle([margin, margin, margin + self.cols * cell_size,
                        margin + self.rows * cell_size], outline="green", width=2)

        # Draw vertical walls
        for i in range(self.rows):
            for j in range(self.cols):
                x, y = j * cell_size + margin, i * cell_size + margin
                if j < self.cols - 1 and self.vertical_walls[i][j]:
                    draw.line([x + cell_size, y, x + cell_size, y + cell_size], "green", width=2)

        # Draw horizontal walls
        for i in range(self.rows):
            for j in range(self.cols):
                x, y = j * cell_size + margin, i * cell_size + margin
                if i < self.rows - 1 and self.horizontal_walls[i][j]:
                    draw.line([x, y + cell_size, x + cell_size, y + cell_size], "green", width=2)

        if with_solution:
            for i in range(len(self.solution_path) - 1):
                x1, y1 = self.solution_path[i][1] * cell_size + margin + cell_size // 2, self.solution_path[i][
                    0] * cell_size + margin + cell_size // 2
                x2, y2 = self.solution_path[i + 1][1] * cell_size + margin + cell_size // 2, self.solution_path[i + 1][
                    0] * cell_size + margin + cell_size // 2
                draw.line([x1, y1, x2, y2], "red", width=2)

        filename = "maze.jpg"
        image1.save(filename)
