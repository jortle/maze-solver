from window import Window
from maze import Maze
import sys
import random


def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    sys.setrecursionlimit(10000)

    maze = Maze(
        margin,
        margin,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
        random.randrange(10000),
    )

    win.maze = maze

    print("Maze created")

    win.wait_for_close()


main()
