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
        self._reset_cells_visited()


    # tries to solve the maze
    # returns True if maze is solved
    # returns False if maze is unsolvable
    def solve(self):
        return self._solve_r(0, 0)
    
    
    # returns True if end of the maze
    # returns False if dead-end
    def _solve_r(self, i, j):
        self._animate()
        
        # marks current cell visited
        self._cells[i][j].visited = True
        
        # returns True if at the end cell
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        # visits left cell if way is open and hasn't been visited        
        if 0 <= i - 1 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            # if path end in dead-end marks with grey line
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        
        # visits right cell
        if i + 1 < len(self._cells) and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)

        # visits top cell
        if 0 <= j - 1 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)

        # visits bottom cell
        if j + 1 < len(self._cells[0]) and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)

        # lets previous cell know this is a dead-end
        return False
        

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
            next_index_list = []
            
            # check adjacent cells and adds unvisited ones to the list
            if 0 <= i - 1 and not self._cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            if i + 1 < len(self._cells) and not self._cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            if 0 <= j - 1 and not self._cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            if j + 1 < len(self._cells[0]) and not self._cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))
            
            # break when every cell is visited
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                break

            # randomly select next cell to visit
            next_index = next_index_list.pop(random.randrange(len(next_index_list)))

            # destroy wall between current and next cell
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_index[0], next_index[1])


    def _reset_cells_visited(self):
        for column in self._cells:
            for cell in column:
                cell.visited = False


    def _draw_cell(self, i, j):
        cell_x1 = self._x1 + i * self._cell_size_x        
        cell_y1 = self._y1 + j * self._cell_size_y
        cell_x2 = self._x1 + (i + 1) * self._cell_size_x
        cell_y2 = self._y1 + (j + 1) * self._cell_size_y

        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)

        self._animate()


    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
