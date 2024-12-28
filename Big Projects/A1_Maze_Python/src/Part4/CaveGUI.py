import tkinter as tk
from tkinter import filedialog, messagebox
from MazeCaveGenerator import CaveGenerator


class CaveApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Cave Generator")
        self.geometry("800x550")

        self.canvas = tk.Canvas(self, width=520, height=520, bg='white')
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        self.control_frame = tk.Frame(self)
        self.control_frame.pack(side=tk.RIGHT, padx=10, pady=10, fill=tk.Y)

        self.row_label = tk.Label(self.control_frame, text="Rows (max 50):")
        self.row_label.grid(row=0, column=0, padx=5, pady=2, sticky="e")

        self.row_entry = tk.Entry(self.control_frame)
        self.row_entry.grid(row=0, column=1, padx=5, pady=2)
        self.row_entry.insert(0, "20")

        self.col_label = tk.Label(self.control_frame, text="Columns (max 50):")
        self.col_label.grid(row=1, column=0, padx=5, pady=2, sticky="e")

        self.col_entry = tk.Entry(self.control_frame)
        self.col_entry.grid(row=1, column=1, padx=5, pady=2)
        self.col_entry.insert(0, "20")

        self.birth_limit_label = tk.Label(self.control_frame, text="Birth limit (0-7):")
        self.birth_limit_label.grid(row=2, column=0, padx=5, pady=2, sticky="e")

        self.birth_limit_entry = tk.Entry(self.control_frame)
        self.birth_limit_entry.grid(row=2, column=1, padx=5, pady=2)
        self.birth_limit_entry.insert(0, "4")

        self.death_limit_label = tk.Label(self.control_frame, text="Death limit (0-7):")
        self.death_limit_label.grid(row=3, column=0, padx=5, pady=2, sticky="e")

        self.death_limit_entry = tk.Entry(self.control_frame)
        self.death_limit_entry.grid(row=3, column=1, padx=5, pady=2)
        self.death_limit_entry.insert(0, "3")

        self.initial_fill_label = tk.Label(self.control_frame, text="Initial fill probability (0-1):")
        self.initial_fill_label.grid(row=4, column=0, padx=5, pady=2, sticky="e")

        self.initial_fill_entry = tk.Entry(self.control_frame)
        self.initial_fill_entry.grid(row=4, column=1, padx=5, pady=2)
        self.initial_fill_entry.insert(0, "0.4")

        self.step_button = tk.Button(self.control_frame, text="Next Step", command=self.next_step)
        self.step_button.grid(row=5, column=0, columnspan=2, pady=5)

        self.auto_button = tk.Button(self.control_frame, text="Auto Step", command=self.auto_step)
        self.auto_button.grid(row=6, column=0, columnspan=2, pady=5)

        self.stop_button = tk.Button(self.control_frame, text="Stop Auto", command=self.stop_auto_step)
        self.stop_button.grid(row=7, column=0, columnspan=2, pady=5)

        self.load_button = tk.Button(self.control_frame, text="Load from File", command=self.load_from_file)
        self.load_button.grid(row=8, column=0, columnspan=2, pady=5)

        self.save_button = tk.Button(self.control_frame, text="Save to File", command=self.save_to_file)
        self.save_button.grid(row=9, column=0, columnspan=2, pady=5)

        self.auto_step_interval_label = tk.Label(self.control_frame, text="Auto step interval (ms):")
        self.auto_step_interval_label.grid(row=10, column=0, padx=5, pady=2, sticky="e")

        self.auto_step_interval_entry = tk.Entry(self.control_frame)
        self.auto_step_interval_entry.grid(row=10, column=1, padx=5, pady=2)
        self.auto_step_interval_entry.insert(0, "500")

        self.generator = None
        self.auto_step_running = False

    def next_step(self):
        if self.generator is None:
            self.show_error("Generate or load a cave first.")
            return
        self.generator.simulate_step()
        self.draw_cave()

    def auto_step(self):
        if self.generator is None:
            self.show_error("Generate or load a cave first.")
            return
        if not self.auto_step_running:
            self.auto_step_running = True
            self.perform_auto_step()

    def perform_auto_step(self):
        if not self.auto_step_running:
            return
        self.next_step()
        interval = int(self.auto_step_interval_entry.get())
        self.after(interval, self.perform_auto_step)

    def stop_auto_step(self):
        self.auto_step_running = False

    def load_from_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if not file_path:
                return

            self.generator = CaveGenerator(1, 1, 0, 0, 0)
            self.generator.load_from_file(file_path)

            if self.generator.rows > 50 or self.generator.cols > 50:
                self.show_error("The cave in the file exceeds the maximum allowed size of 50x50.")
                return

            self.draw_cave()

        except Exception as e:
            self.show_error(f"Error loading file: {str(e)}")

    def save_to_file(self):
        if self.generator is None:
            self.show_error("No cave generated or loaded to save.")
            return

        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if not file_path:
                return

            self.generator.save_to_file(file_path)

        except Exception as e:
            self.show_error(f"Error saving file: {str(e)}")

    def draw_cave(self):
        if self.generator is None:
            return

        self.canvas.delete("all")
        cell_size = min(500 // self.generator.rows, 500 // self.generator.cols)
        margin = 10

        for i in range(self.generator.rows):
            for j in range(self.generator.cols):
                x, y = j * cell_size + margin, i * cell_size + margin
                if self.generator.grid[i][j] == 1:
                    self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill='black')
                else:
                    self.canvas.create_rectangle(x, y, x + cell_size, y + cell_size, fill='white')

    def show_error(self, message):
        messagebox.showerror("Error", message)


if __name__ == "__main__":
    app = CaveApp()
    app.mainloop()
