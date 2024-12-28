import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import filedialog, simpledialog
from Part2.MazeEller import MazeGenerator
from MazeSolver import MazeSolver


class MazeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Generator & Solver")
        self.geometry("750x750")

        self.canvas = tk.Canvas(self, width=520, height=520, bg='white')
        self.canvas.pack(pady=10)

        self.control_frame = tk.Frame(self)
        self.control_frame.pack(pady=10)

        self.row_label = tk.Label(self.control_frame, text="Rows (max 50):")
        self.row_label.grid(row=0, column=0, padx=5)

        self.row_entry = tk.Entry(self.control_frame)
        self.row_entry.grid(row=0, column=1, padx=5)
        self.row_entry.insert(0, "20")

        self.col_label = tk.Label(self.control_frame, text="Columns (max 50):")
        self.col_label.grid(row=1, column=0, padx=5)

        self.col_entry = tk.Entry(self.control_frame)
        self.col_entry.grid(row=1, column=1, padx=5)
        self.col_entry.insert(0, "20")

        self.generate_button = tk.Button(self.control_frame, text="Generate Maze", command=self.generate_maze)
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.load_button = tk.Button(self.control_frame, text="Load from File", command=self.load_from_file)
        self.load_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.save_button = tk.Button(self.control_frame, text="Save to File", command=self.save_to_file)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.solve_button = tk.Button(self.control_frame, text="Solve Maze", command=self.solve_maze)
        self.solve_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.generator = None
        self.solver = None

    def generate_maze(self):
        try:
            rows = int(self.row_entry.get())
            cols = int(self.col_entry.get())
            if rows <= 0 or cols <= 0 or rows > 50 or cols > 50:
                raise ValueError
        except ValueError:
            self.show_error("Invalid input. Please enter positive integers not exceeding 50.")
            return

        self.canvas.delete("all")

        self.generator = MazeGenerator(rows, cols)
        self.generator.generate_maze()

        cell_size = min(500 // rows, 500 // cols)
        margin = 10

        self.draw_maze(self.generator, cell_size, margin)

    def load_from_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if not file_path:
                return

            self.canvas.delete("all")

            self.generator = MazeGenerator(1, 1)
            self.generator.load_from_file(file_path)

            if self.generator.rows > 50 or self.generator.cols > 50:
                self.show_error("The maze in the file exceeds the maximum allowed size of 50x50.")
                return

            cell_size = min(500 // self.generator.rows, 500 // self.generator.cols)
            margin = 10

            self.draw_maze(self.generator, cell_size, margin)

        except Exception as e:
            self.show_error(f"Error loading file: {str(e)}")

    def save_to_file(self):
        if self.generator is None:
            self.show_error("No maze generated or loaded to save.")
            return

        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if not file_path:
                return

            self.generator.save_to_file(file_path)

        except Exception as e:
            self.show_error(f"Error saving file: {str(e)}")

    def solve_maze(self):
        if self.generator is None:
            self.show_error("No maze generated or loaded to solve.")
            return

        try:
            start = self.get_point("Enter start point (row, col):")
            end = self.get_point("Enter end point (row, col):")
            if not start or not end:
                return

            self.solver = MazeSolver(self.generator.vertical_walls, self.generator.horizontal_walls)
            path = self.solver.solve_maze(start, end)

            if path:
                cell_size = min(500 // self.generator.rows, 500 // self.generator.cols)
                margin = 10
                self.draw_solution(path, cell_size, margin)
            else:
                self.show_error("No solution found for the maze.")
        except Exception as e:
            self.show_error(f"Error solving maze: {str(e)}")

    def get_point(self, prompt):
        point_str = simpledialog.askstring("Input", prompt)
        if point_str:
            try:
                row, col = map(int, point_str.split(","))
                if 0 <= row < self.generator.rows and 0 <= col < self.generator.cols:
                    return (row, col)
            except ValueError:
                pass
        self.show_error("Invalid point. Please enter in format 'row,col' within maze bounds.")
        return None

    def draw_maze(self, generator, cell_size, margin):
        self.canvas.delete("all")
        # Draw vertical walls
        for i in range(generator.rows):
            for j in range(generator.cols):
                x, y = j * cell_size + margin, i * cell_size + margin
                if j < generator.cols - 1 and generator.vertical_walls[i][j]:
                    self.canvas.create_line(x + cell_size, y, x + cell_size, y + cell_size, width=2)

        # Draw horizontal walls
        for i in range(generator.rows):
            for j in range(generator.cols):
                x, y = j * cell_size + margin, i * cell_size + margin
                if i < generator.rows - 1 and generator.horizontal_walls[i][j]:
                    self.canvas.create_line(x, y + cell_size, x + cell_size, y + cell_size, width=2)

        # Draw outer walls
        self.canvas.create_rectangle(margin, margin, margin + generator.cols * cell_size,
                                     margin + generator.rows * cell_size, width=2)

    def draw_solution(self, path, cell_size, margin):
        for i in range(len(path) - 1):
            x1, y1 = path[i][1] * cell_size + margin + cell_size // 2, path[i][0] * cell_size + margin + cell_size // 2
            x2, y2 = path[i + 1][1] * cell_size + margin + cell_size // 2, path[i + 1][0] * cell_size + margin + cell_size // 2
            self.canvas.create_line(x1, y1, x2, y2, fill="red", width=2)

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
