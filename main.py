from window import Window, Point, Line


def main():
    win = Window(800, 600)

    point1 = Point(100, 100)
    point2 = Point(200, 200)
    point3 = Point(300, 300)

    line1 = Line(point1, point2)
    line2 = Line(point2, point3)
    line3 = Line(point3, point1)

    win.draw_line(line1, "red")
    win.draw_line(line2, "blue")
    win.wait_for_close()


main()
