from graphics import Window, Line, Point
from cell import Cell


def main():
        win = Window(800, 600)

        c = Cell(win)


        c.draw(100, 100, 200, 200)


        win.wait_for_close()          

main()
