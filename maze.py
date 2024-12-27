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
        window=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = window        
        self._cells = []

        if seed:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

    def _create_cells(self):        
        for i in range(self._num_cols):
            self._cells.append([])
            for j in range(self._num_rows):
                self._cells[i].append(Cell(self._win))
                self._draw_cell(i, j)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit_list = []
            if 0 <= i - 1 < len(self._cells) and not self._cells[i - 1][j].visited:
                to_visit_list.append(self._cells[i - 1][j])
            if 0 <= i + 1 < len(self._cells) and not self._cells[i + 1][j].visited:
                to_visit_list.append(self._cells[i + 1][j])
            if 0 <= j - 1 < len(self._cells[0]) and not self._cells[i][j - 1].visited:
                to_visit_list.append(self._cells[i][j - 1])
            if 0 <= j + 1 < len(self._cells[0]) and not self._cells[i][j + 1].visited:
                to_visit_list.append(self._cells[i][j + 1])
            
            if len(to_visit_list) == 0:
                self._draw_cell(i, j)
                break

            to_visit = to_visit_list.pop(random.randrange(len(to_visit_list)))
            if self._cells[i][j]._x1 == to_visit._x1:
                if self._cells[i][j]._y1 < to_visit._y1:
                    self._cells[i][j].has_bottom_wall = False
                    self._draw_cell(i, j)
                    to_visit.has_top_wall = False
                    self._draw_cell(i, j + 1)
                    self._break_walls_r(i, j + 1)
                else:
                    self._cells[i][j].has_top_wall = False
                    self._draw_cell(i, j)
                    to_visit.has_bottom_wall = False
                    self._draw_cell(i, j - 1)
                    self._break_walls_r(i, j - 1)
            else:
                if self._cells[i][j]._x1 < to_visit._x1:
                    self._cells[i][j].has_right_wall = False
                    self._draw_cell(i, j)
                    to_visit.has_left_wall = False
                    self._draw_cell(i + 1, j)
                    self._break_walls_r(i + 1, j)
                else:
                    self._cells[i][j].has_left_wall = False
                    self._draw_cell(i, j)
                    to_visit.has_right_wall = False
                    self._draw_cell(i - 1, j)
                    self._break_walls_r(i - 1, j)
            
            

            


    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + i * self._cell_size_x        
        cell_y1 = self._y1 + j * self._cell_size_y
        cell_x2 = self._x1 + (i + 1) * self._cell_size_x
        cell_y2 = self._y1 + (j + 1) * self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)

        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.01)
        

