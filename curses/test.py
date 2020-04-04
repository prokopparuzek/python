import curses

screen = curses.initscr()
curses.start_color()
curses.use_default_colors()
screen.keypad(True)
curses.noecho()
curses.cbreak()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_CYAN)
while True:
    c = screen.getch()
    screen.addch(0, 0, c, curses.color_pair(1))
    if c == ord('S'):
        break
    screen.refresh()
curses.endwin()
