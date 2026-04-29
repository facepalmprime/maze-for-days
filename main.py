from graphics import Window, Line, Point
from cell import Cell


def main():
        win = Window(800, 600)

        c = Cell(win)


        c.draw(100, 100, 200, 200)

        c2 = Cell(win)
        c2.has_top_wall = False
        c2.draw(100, 50, 150, 100)


        c3 = Cell(win)
        c3.draw(100, 100, 150, 150)
        c2.draw_move(c3, undo=False)


        win.wait_for_close()          

main()
