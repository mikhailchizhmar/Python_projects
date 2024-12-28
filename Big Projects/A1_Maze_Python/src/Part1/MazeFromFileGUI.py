import tkinter as tk
from tkinter import filedialog

from MazeFromFile import Maze


class MazeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Maze Viewer")
        self.geometry("600x600")

        self.canvas = tk.Canvas(self, width=520, height=520, bg='white')
        self.canvas.pack(pady=10)

        self.control_frame = tk.Frame(self)
        self.control_frame.pack(pady=10)

        self.load_button = tk.Button(self.control_frame, text="Load from File", command=self.load_from_file)
        self.load_button.grid(row=2, column=0, columnspan=2, pady=5)

        self.generator = None

    def load_from_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if not file_path:
                return

            self.canvas.delete("all")

            self.generator = Maze(1, 1)
            self.generator.load_from_file(file_path)

            if self.generator.rows > 50 or self.generator.cols > 50:
                self.show_error("The maze in the file exceeds the maximum allowed size of 50x50.")
                return

            cell_size = min(500 // self.generator.rows, 500 // self.generator.cols)
            margin = 10

            self.draw_maze(self.generator, cell_size, margin)

        except Exception as e:
            self.show_error(f"Error loading file: {str(e)}")

    def draw_maze(self, generator, cell_size, margin):
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
