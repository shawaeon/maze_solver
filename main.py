from graphics import Window, Point, Line
from cell import Cell


def main():
    win = Window(800, 600)  

    cell1 = Cell(window=win)
    cell1.has_right_wall=False
    cell1.draw(250, 250, 270, 270)
    
    cell2 = Cell(window=win)
    cell2.has_left_wall =False
    cell2.has_bottom_wall =False
    cell2.draw(270, 250, 290, 270)

    cell3 = Cell(window=win)
    cell3.has_top_wall =False
    cell3.draw(270, 270, 290, 290)

    cell1.draw_move(cell2)
    cell2.draw_move(cell3)

    win.wait_for_close()




if __name__ == "__main__":
    main()
