"""keypress - A module for detectiong a single keypress"""

try:
    import msvcrt

    def getkey():
        return msvcrt.getch()

except ImportError:

    import sys
    import tty
    import termios

    def getkey():
        fd = sys.stdin.fileno()
        original_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRIAN, original_attributes)
        return ch
