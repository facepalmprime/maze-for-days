from graphics import Line, Point
class Cell: 
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
     
    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
             start_point = Point(x1, y1)
             end_point = Point(x1, y2)
             left_line = Line(start_point, end_point)
             self.__win.draw_line(left_line, "black")
        
        if self.has_right_wall:
             start_point = Point(x2, y1)
             end_point = Point(x2, y2)
             right_line = Line(start_point, end_point)
             self.__win.draw_line(right_line, "black")
        
        if self.has_top_wall:
             start_point = Point(x1, y1)
             end_point = Point(x2, y1)
             top_line = Line(start_point, end_point)
             self.__win.draw_line(top_line, "black")
        
        if self.has_bottom_wall:
             start_point = Point(x1, y2)
             end_point = Point(x2, y2)
             bottom_line = Line(start_point, end_point)
             self.__win.draw_line(bottom_line, "black")
