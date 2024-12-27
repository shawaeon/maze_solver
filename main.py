from graphics import Window, Point, Line
from cell import Cell
from maze import Maze


def main():


    num_rows = 10
    num_cols = 14
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - (2 * margin)) / num_cols
    cell_size_y = (screen_y - (2 * margin)) / num_rows

    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, window=win)
    print("Maze created.")

    is_solvable = maze.solve()
    if is_solvable:
        print("Maze solved!")
    else:
        print("Maze is not solvable.")

    win.wait_for_close()




if __name__ == "__main__":
    main()
