from window import Window
import sys


def main():
    screen_x = 1500
    screen_y = 900
    win = Window(screen_x, screen_y)
    sys.setrecursionlimit(10000)

    print("Maze created")

    win.wait_for_close()


main()
