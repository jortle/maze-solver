import tkinter as tk
from tkinter import Tk, BOTH, Canvas, ttk
from maze import Maze
import random


class Window:
    def __init__(self, width, height):
        # dimensions
        self.width = width
        self.height = height
        self.seed = random.randrange(10000)
        # whole window root

        self.__root = Tk()
        self.__root.title("Maze Solver")

        # Canvas for drawing
        self.__canvas = Canvas(
            self.__root, bg="white", height=self.height, width=self.width
        )
        self.__canvas.pack(fill=BOTH, expand=1)

        self.setup_widgets()
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        # creates buttons and other widgets

    def setup_widgets(self):
        # buttons
        # solve button
        solve_button = ttk.Button(
            self.__root, text="Solve Maze", command=self._solve_button
        )
        self.__canvas.create_window(
            self.width * 0.5, 25, anchor=tk.CENTER, window=solve_button
        )

        # New Maze button

        new_maze_button = ttk.Button(
            self.__root, text="New Maze", command=self._new_maze_button
        )
        self.__canvas.create_window(
            self.width * 0.1, 25, anchor=tk.CENTER, window=new_maze_button
        )

        # pause/play animation button

        # reset maze button
        reset_button = ttk.Button(
            self.__root, text="Reset Maze", command=self._reset_button
        )
        self.__canvas.create_window(
            self.width * 0.2, 25, anchor=tk.CENTER, window=reset_button
        )

        # switch algorithm button
        switch_algorithm_button = ttk.Button(
            self.__root, text="Switch Algorithm", command=self._switch_algorithm
        )

        self.__canvas.create_window(
            self.width * 0.6, 25, anchor=tk.CENTER, window=switch_algorithm_button
        )
        # algorithm label

        algorithm_label = tk.Label(self.__root, text="Algorithm: {self.maze.algorithm}")
        self.__canvas.create_window(
            self.width * 0.5, self.height - 25, anchor=tk.CENTER, window=algorithm_label
        )
        # entry box for seed

        # self.seed_entry = ttk.Entry(self.__root)
        # self.__canvas.create_window(
        #    self.width * 0.2, self.height - 25, anchor=tk.CENTER, window=self.seed_entry
        # )

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def _solve_button(self):
        if self.maze is None:
            return
        print(self.maze.algorithm)
        self.maze.solve_alg()

    def _new_maze_button(self):
        self._reset_button()
        # if self.seed_entry.get() is None:
        self.seed = random.randrange(10000)
        # else:
        #    self.seed = self.seed_entry.get()
        # self._create_maze()

    def _pause_button(self):
        pass

    def _reset_button(self):
        self.__canvas.delete("all")
        self.setup_widgets()
        self._create_maze()

    def _create_maze(self):
        self.num_rows = 19
        self.num_cols = 38
        self.margin = 50
        self.cell_size_x = (self.width - 2 * self.margin) / self.num_cols
        self.cell_size_y = (self.height - 2 * self.margin) / self.num_rows
        maze = Maze(
            self.margin,
            self.margin,
            self.num_rows,
            self.num_cols,
            self.cell_size_x,
            self.cell_size_y,
            self,
            self.seed,
        )
        self.maze = maze

    def _switch_algorithm(self):
        if self.maze.algorithm == "dfs_r":
            self.maze.algorithm = "bfs"
        elif self.maze.algorithm == "bfs":
            self.maze.algorithm = "dfs_r"
