import tkinter as tk
from tkinter import Tk, BOTH, Canvas, ttk


class Window:
    def __init__(self, width, height):
        # maze for method access
        self.maze = None
        # whole window root

        self.__root = Tk()
        self.__root.title("Maze Solver")

        # Canvas for drawing
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)

        # buttons
        # solve button
        solve_button = ttk.Button(self.__root, text="Solve Maze", command=self.solve)
        self.__canvas.create_window(400, 25, anchor=tk.CENTER, window=solve_button)
        # random seed

        # entry box for seed

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

    def solve(self):
        if self.maze is None:
            return
        self.maze.solve()
