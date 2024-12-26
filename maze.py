from cell import Cell
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
        window,
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window
        self._cells = []

        self._create_cells()



    def _create_cells(self):        
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append([])
                self._cells[i][j] = self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + i * self._cell_size_x        
        cell_y1 = self._y1 + j * self._cell_size_y
        cell_x2 = self._x1 + (i + 1) * self._cell_size_x
        cell_y2 = self._y1 + (j + 1) * self._cell_size_y

        new_cell = Cell(self._win)
        new_cell.draw(cell_x1, cell_y1, cell_x2, cell_y2)

        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)
        

