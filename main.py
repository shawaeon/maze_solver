from graphics import Window, Point, Line


def main():
    win = Window(800, 600)  

    l = Line(Point(50, 50), Point(600, 400))
    win.draw_line(l, "green")

    win.wait_for_close()




if __name__ == "__main__":
    main()
