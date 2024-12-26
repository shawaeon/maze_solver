from graphics import Line, Point

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None        

        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        if self.has_left_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x1, self._y2)), fill_color="white")
        if self.has_right_wall:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x2, self._y1), Point(self._x2, self._y2)), fill_color="white")    
        if self.has_top_wall:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y1), Point(self._x2, self._y1)), fill_color="white")    
        if self.has_bottom_wall:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)))
        else:
            self._win.draw_line(Line(Point(self._x1, self._y2), Point(self._x2, self._y2)), fill_color="white")

    def draw_move(self, to_cell, undo=False):
        
        fill_color = "red"
        if undo:
            fill_color = "gray"

        center_x1 = self._x1 + abs(self._x2 - self._x1) // 2
        center_y1 = self._y1 + abs(self._y2 - self._y1) // 2

        center_x2 = to_cell._x1 + abs(to_cell._x2 - to_cell._x1) // 2
        center_y2 = to_cell._y1 + abs(to_cell._y2 - to_cell._y1) // 2


        self._win.draw_line(Line(Point(center_x1, center_y1), Point(center_x2, center_y2)), fill_color=fill_color)

