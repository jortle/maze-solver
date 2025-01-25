from cell import Cell
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
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []
        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for col in range(self.__num_cols):
            col_list = []
            for row in range(self.__num_rows):
                col_list.append(Cell(self.__win))
            self._cells.append(col_list)
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self._draw_cell(col, row)

    def _draw_cell(self, col, row):
        if self.__win is None:
            return
        x1 = self.__cell_size_x * col + self.__x1
        y1 = self.__cell_size_y * row + self.__y1
        x2 = x1 + self.__cell_size_x
        y2 = y1 + self.__cell_size_y
        self._cells[col][row].draw(x1, y1, x2, y2)
        self.animate()

    def animate(self):
        if self.__win is None:
            return
        self.__win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j]._visited = True
        while True:
            to_visit = []

            if i > 0 and not self._cells[i - 1][j]._visited:
                to_visit.append((i - 1, j))
            if i < self.__num_cols - 1 and not self._cells[i + 1][j]._visited:
                to_visit.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1]._visited:
                to_visit.append((i, j - 1))
            if j < self.__num_rows - 1 and not self._cells[i][j + 1]._visited:
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
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self._cells[i][j]._visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self.animate()

        self._cells[i][j]._visited = True
        # check for end
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        # try each direction
        # left
        if (
            i > 0
            and not self._cells[i - 1][j]._visited
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # right
        if (
            i < self.__num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j]._visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # up
        if (
            j > 0
            and not self._cells[i][j - 1]._visited
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # down
        if (
            j < self.__num_rows - 1
            and not self._cells[i][j + 1]._visited
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
