import random
import tkinter as tk
from tkinter import filedialog


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

    def is_move_valid(self, x, y, direction):
        if direction == "up":
            return y > 0 and not self.horizontal_walls[y - 1][x]
        elif direction == "down":
            return y < self.rows - 1 and not self.horizontal_walls[y][x]
        elif direction == "left":
            return x > 0 and not self.vertical_walls[y][x - 1]
        elif direction == "right":
            return x < self.cols - 1 and not self.vertical_walls[y][x]
        return False

    def get_state_index(self, x, y):
        return y * self.cols + x

    def get_position_from_index(self, index):
        return index % self.cols, index // self.cols


class QAgent:
    # https://medium.com/@alaminhnab4/understanding-q-learning-in-reinforcement-learning-3b0e10223ae5
    # https://www.freecodecamp.org/news/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc/
    # https://towardsdatascience.com/reinforcement-learning-explained-visually-part-4-q-learning-step-by-step-b65efb731d3e

    # https://dev.to/akshayballal/maze-solving-robot-with-reinforcement-learning-part-2-5enc

    def __init__(self, maze, end_position, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.maze = maze
        self.end_position = end_position
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = [[0 for _ in range(4)] for _ in range(self.maze.rows * self.maze.cols)]
        self.actions = ["up", "down", "left", "right"]

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.actions)
        else:
            return self.actions[self.q_table[state].index(max(self.q_table[state]))]

    def update_q_value(self, state, action, reward, next_state):
        action_index = self.actions.index(action)
        next_max = max(self.q_table[next_state])
        self.q_table[state][action_index] += self.alpha * (
                reward + self.gamma * next_max - self.q_table[state][action_index])

    def learn(self, episodes=1000):
        for episode in range(episodes):
            print(f"Starting episode {episode + 1}")
            state = self.maze.get_state_index(random.randint(0, self.maze.cols - 1),
                                              random.randint(0, self.maze.rows - 1))
            steps = 0
            while state != self.maze.get_state_index(*self.end_position):
                x, y = self.maze.get_position_from_index(state)
                action = self.choose_action(state)
                if self.maze.is_move_valid(x, y, action):
                    if action == "up":
                        next_state = self.maze.get_state_index(x, y - 1)
                    elif action == "down":
                        next_state = self.maze.get_state_index(x, y + 1)
                    elif action == "left":
                        next_state = self.maze.get_state_index(x - 1, y)
                    elif action == "right":
                        next_state = self.maze.get_state_index(x + 1, y)

                    reward = 1 if next_state == self.maze.get_state_index(*self.end_position) else -0.1
                    self.update_q_value(state, action, reward, next_state)
                    state = next_state
                else:
                    reward = -1
                    self.update_q_value(state, action, reward, state)
                steps += 1
                if steps > 1000:  # Safety measure to prevent infinite loop
                    print("Breaking out of loop, step limit reached.")
                    break

    def get_optimal_path(self, start_position):
        path = []
        state = self.maze.get_state_index(*start_position)
        while state != self.maze.get_state_index(*self.end_position):
            x, y = self.maze.get_position_from_index(state)
            path.append((x, y))
            action_index = self.q_table[state].index(max(self.q_table[state]))
            action = self.actions[action_index]
            if action == "up":
                state = self.maze.get_state_index(x, y - 1)
            elif action == "down":
                state = self.maze.get_state_index(x, y + 1)
            elif action == "left":
                state = self.maze.get_state_index(x - 1, y)
            elif action == "right":
                state = self.maze.get_state_index(x + 1, y)
            if len(path) > 10000:  # Safety measure to prevent infinite loop
                print("Breaking out of path construction, step limit reached.")
                break
        path.append(self.end_position)
        return path


class MazeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Solver")
        self.geometry("750x750")

        self.canvas = tk.Canvas(self, width=520, height=520, bg='white')
        self.canvas.pack(pady=10)

        self.control_frame = tk.Frame(self)
        self.control_frame.pack(pady=10)

        self.load_button = tk.Button(self.control_frame, text="Load Maze", command=self.load_maze)
        self.load_button.pack(side=tk.LEFT, padx=5)

        self.start_label = tk.Label(self.control_frame, text="Start (x, y):")
        self.start_label.pack(side=tk.LEFT, padx=5)

        self.start_entry = tk.Entry(self.control_frame)
        self.start_entry.pack(side=tk.LEFT, padx=5)

        self.solve_button = tk.Button(self.control_frame, text="Solve Maze", command=self.solve_maze)
        self.solve_button.pack(side=tk.LEFT, padx=5)

        self.maze = None
        self.agent = None
        self.end_position = None

    def load_maze(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        self.maze = Maze(0, 0)
        self.maze.load_from_file(file_path)
        self.end_position = (self.maze.cols - 1, self.maze.rows - 1)  # End position is bottom right corner

        self.agent = QAgent(self.maze, self.end_position)
        print("Starting learning process")
        self.agent.learn(episodes=10000)
        print("Learning process completed")

        self.draw_maze()

    def draw_maze(self):
        self.canvas.delete("all")
        cell_size = min(500 // self.maze.rows, 500 // self.maze.cols)
        margin = 10

        # Draw vertical walls
        for i in range(self.maze.rows):
            for j in range(self.maze.cols):
                x, y = j * cell_size + margin, i * cell_size + margin
                if j < self.maze.cols - 1 and self.maze.vertical_walls[i][j]:
                    self.canvas.create_line(x + cell_size, y, x + cell_size, y + cell_size, width=2)

        # Draw horizontal walls
        for i in range(self.maze.rows):
            for j in range(self.maze.cols):
                x, y = j * cell_size + margin, i * cell_size + margin
                if i < self.maze.rows - 1 and self.maze.horizontal_walls[i][j]:
                    self.canvas.create_line(x, y + cell_size, x + cell_size, y + cell_size, width=2)

        self.canvas.create_rectangle(margin, margin, margin + self.maze.cols * cell_size,
                                     margin + self.maze.rows * cell_size, width=2)

    def solve_maze(self):
        try:
            start_x, start_y = map(int, self.start_entry.get().split(","))
            if start_x < 0 or start_x >= self.maze.cols or start_y < 0 or start_y >= self.maze.rows:
                raise ValueError("Start position out of bounds.")
        except ValueError as e:
            self.show_error("Invalid start position. Please enter two integers separated by a comma.")
            return

        path = self.agent.get_optimal_path((start_x, start_y))
        self.draw_path(path)

    def draw_path(self, path):
        cell_size = min(500 // self.maze.rows, 500 // self.maze.cols)
        margin = 10
        for i in range(len(path) - 1):
            x1, y1 = path[i]
            x2, y2 = path[i + 1]
            self.canvas.create_line(
                x1 * cell_size + margin + cell_size // 2,
                y1 * cell_size + margin + cell_size // 2,
                x2 * cell_size + margin + cell_size // 2,
                y2 * cell_size + margin + cell_size // 2,
                fill="green",
                width=2
            )

    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("Error")
        error_window.geometry("300x100")

        label = tk.Label(error_window, text=message)
        label.pack(pady=20)

        button = tk.Button(error_window, text="OK", command=error_window.destroy)
        button.pack()


if __name__ == "__main__":
    app = MazeApp()
    app.mainloop()
