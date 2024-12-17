from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)  

    cell = Cell(window=win)
    cell.has_right_wall=False
    cell.draw(250, 250, 270, 270)
    
    cell = Cell(window=win)
    cell.has_left_wall =False
    cell.has_bottom_wall=False
    cell.draw(270, 250, 290, 270)
    
    cell = Cell(win)
    cell.has_top_wall=False
    cell.has_bottom_wall=False
    cell.draw(270, 270, 290, 290)
    
    cell = Cell(win)
    cell.has_top_wall=False
    cell.draw(270, 290, 290, 310)

    win.wait_for_close()




if __name__ == "__main__":
    main()
