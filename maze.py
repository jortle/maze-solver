from window import Cell
import time


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
    ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self._cells = []

        self._create_cells()
        self._break_entrance_and_exit()

    def _create_cells(self):
        for col in range(self.__num_cols):
            col_list = []
            for row in range(self.__num_rows):
                col_list.append(Cell(self.__win))
            self._cells.append(col_list)
        for col in range(self.__num_cols):
            for row in range(self.__num_rows):
                self._draw_cells(col, row)

    def _draw_cells(self, col, row):
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
        time.sleep(0.5)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self._draw_cells(self.__num_cols - 1, self.__num_rows - 1)
