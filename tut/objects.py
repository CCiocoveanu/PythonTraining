def banner(border='-'):
    message = input("Type stuff: ")
    line = border * len(message)
    print(line)
    print(message)
    print(line)


if __name__ == "__main__":
    banner("-")
