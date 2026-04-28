from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        
        self.__running = False
        self.width = width
        self.height = height
        self.__root = Tk()
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__root.title("Maze for Days")
        self.__canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)
    
    def draw_line(self, line, fill_color):
         line.draw(self.__canvas, fill_color)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
            

    def close(self):
        self.__running = False





class Point:
     def __init__(self, x, y):
          self.x = x
          self.y = y




class Line:
     def __init__(self, point1, point2):
          self.point1 = point1
          self.point2 = point2
          
     def draw(self, canvas, fill_color):
          canvas.create_line(
               self.point1.x,
               self.point1.y,
               self.point2.x,
               self.point2.y,
               fill=fill_color,
               width=2
          )

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
         


def main():
        win = Window(800, 600)

        c = Cell(win)


        c.draw(100, 100, 200, 200)


        win.wait_for_close()          

main()