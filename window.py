import tkinter as tk
from tkinter import Tk, BOTH, Canvas, ttk
from maze import Maze
import random


class Window:
    def __init__(self, width, height):
        # dimensions
        self.width = width
        self.height = height

        # whole window root

        self.__root = Tk()
        self.__root.title("Maze Solver")

        # Canvas for drawing
        self.__canvas = Canvas(
            self.__root, bg="white", height=self.height, width=self.width
        )
        self.__canvas.pack(fill=BOTH, expand=1)

        # buttons
        # solve button
        solve_button = ttk.Button(
            self.__root, text="Solve Maze", command=self._solve_button
        )
        self.__canvas.create_window(
            self.width / 2, 25, anchor=tk.CENTER, window=solve_button
        )

        # New Maze button

        new_maze_button = ttk.Button(
            self.__root, text="New Maze", command=self._new_maze_button
        )
        self.__canvas.create_window(
            self.width / 4, 25, anchor=tk.CENTER, window=new_maze_button
        )

        # pause/play animation button

        # reset maze button

        # entry box for seed

        # functuonal stuff
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

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
        self.maze.solve()

    def _new_maze_button(self):
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
            random.randrange(10000),
        )

        self.maze = maze

    def _pause_button(self):
        pass

    def _reset_button(self):
        pass
