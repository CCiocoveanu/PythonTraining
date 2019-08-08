import sys
import os


def convert(s):
    if not isinstance(s, str):
        raise TypeError("Argument bust be a string")

    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise


def make_at(path, dir_name):
    original_path = os.getcwd()  # current working directory
    try:
        os.chdir(path)  # change dir
        os.mkdir(dir_name)  # make dir
    except OSError as e:
        print(e, file=sys.stderr)
        raise
    finally:
        os.chdir(original_path)

# wait for "press any key to continue:
# windows: msvcrt
# unix: tty or termios

