class MazeSolver:
    def __init__(self, vertical_walls, horizontal_walls):
        self.vertical_walls = vertical_walls
        self.horizontal_walls = horizontal_walls
        self.rows = len(vertical_walls)
        self.cols = len(vertical_walls[0])

    def is_valid_point(self, point):
        row, col = point
        return 0 <= row < self.rows and 0 <= col < self.cols

    def solve_maze(self, start, end):
        if not self.is_valid_point(start) or not self.is_valid_point(end):
            raise ValueError("Start or end point is out of maze bounds.")
        stack = [(start, [start])]
        visited = set()

        while stack:
            (current_cell, path) = stack.pop()
            if current_cell in visited:
                continue
            visited.add(current_cell)

            if current_cell == end:
                return path

            for neighbor in self.get_neighbors(current_cell):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))

        return None

    def get_neighbors(self, cell):
        row, col = cell
        neighbors = []

        if row > 0 and not self.horizontal_walls[row - 1][col]:
            neighbors.append((row - 1, col))
        if row < self.rows - 1 and not self.horizontal_walls[row][col]:
            neighbors.append((row + 1, col))
        if col > 0 and not self.vertical_walls[row][col - 1]:
            neighbors.append((row, col - 1))
        if col < self.cols - 1 and not self.vertical_walls[row][col]:
            neighbors.append((row, col + 1))

        return neighbors
