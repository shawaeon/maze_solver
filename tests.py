import unittest
from graphics import Window
from maze import Maze


class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        win = Window(800, 600)

        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    
    def test_maze_small(self):
        win = Window(800, 600)

        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)
        
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_entrace_and_exit(self):
        win = Window(800, 600)

        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)

        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[num_cols - 1][num_rows - 1].has_bottom_wall, False)

    def test_maze_visited_reset(self):
        win = Window(800, 600)

        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10, win)

        m1._cells[0][0].visited = True
        m1._reset_cells_visited()
        
        self.assertEqual(m1._cells[0][0].visited, False)

if __name__ == "__main__":
    unittest.main()