import random
from graphics import Line, Point
class Cell: 
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = win
        self.visited = False
     
    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
               return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2


        if self.has_left_wall:
             start_point = Point(x1, y1)
             end_point = Point(x1, y2)
             left_line = Line(start_point, end_point)
             self.__win.draw_line(left_line, "black")
        else:
             line = Line(Point(x1, y1), Point(x1, y2)) 
             self.__win.draw_line(line, "#d9d9d9")
        
        if self.has_right_wall:
             start_point = Point(x2, y1)
             end_point = Point(x2, y2)
             right_line = Line(start_point, end_point)
             self.__win.draw_line(right_line, "black")
        else:
             line = Line(Point(x2, y1), Point(x2, y2)) 
             self.__win.draw_line(line, "#d9d9d9")
        
        if self.has_top_wall:
             start_point = Point(x1, y1)
             end_point = Point(x2, y1)
             top_line = Line(start_point, end_point)
             self.__win.draw_line(top_line, "black")
        else:
             line = Line(Point(x1, y1), Point(x2, y1)) 
             self.__win.draw_line(line, "#d9d9d9")
        
        if self.has_bottom_wall:
             start_point = Point(x1, y2)
             end_point = Point(x2, y2)
             bottom_line = Line(start_point, end_point)
             self.__win.draw_line(bottom_line, "black")
        
        else:
             line = Line(Point(x1, y2), Point(x2, y2)) 
             self.__win.draw_line(line, "#d9d9d9") 
     
    def draw_move(self, to_cell, undo=False):
          if self.__win is None:
               return
          x_center_1 = (self.__x1 + self.__x2) /2
          y_center_1 = (self.__y1 + self.__y2) /2
          x_center_2 = (to_cell.__x1 + to_cell.__x2) /2
          y_center_2 = (to_cell.__y1 + to_cell.__y2) /2
          if undo:
               fill_color = "gray"
          else:
               fill_color = "red"
          p1 = Point(x_center_1, y_center_1)
          p2 = Point(x_center_2, y_center_2)

          line = Line(p1, p2)


          self.__win.draw_line(line, fill_color)
     
       


         
         
        
         
         
         
         
         
         
         
         