from cell import Cell
from algorithms import dfs_r, bfs
import time
import random


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        print(self.num_rows, self.num_cols)
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        self.algorithm = "dfs_r"
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self.num_cols):
            col_list = []
            for row in range(self.num_rows):
                col_list.append(Cell(self.__win))
            self._cells.append(col_list)
        for col in range(self.num_cols):
            for row in range(self.num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self.__win is None:
            return
        x1 = self.__cell_size_x * col + self.__x1
        y1 = self.__cell_size_y * row + self.__y1
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[col][row].draw(x1, y1, x2, y2)

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []

            if i > 0 and not self._cells[i - 1][j]._visited:
                to_visit.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j]._visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1]._visited:
                to_visit.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1]._visited:
                to_visit.append((i, j + 1))

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            next_cell_direction = random.randrange(len(to_visit))
            next_cell = to_visit[next_cell_direction]

            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_cell[0], next_cell[1])

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j]._visited = False

    def solve_alg(self):
        self.algorithm = "dfs_r"
        if self.algorithm == "dfs_r":
            return dfs_r(self, 0, 0)
        elif self.algorithm == "bfs":
            return bfs(self, 0, 0)
