from window import Window, Cell


def main():
    win = Window(800, 600)

    cell2 = Cell(win)
    cell2.has_left_wall = False
    cell2.has_bottom_wall = False
    cell2.draw(300, 200, 400, 300)

    cell1 = Cell(win)
    cell1.has_right_wall = False
    cell1.draw(200, 200, 300, 300)

    cell1.draw_move(cell2)

    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.draw(300, 300, 400, 400)

    cell2.draw_move(cell3)

    win.wait_for_close()


main()
