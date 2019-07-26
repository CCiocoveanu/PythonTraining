"""
str | list | dict | tuple | range | set
"""


def tuple_ex():  # tuple - immutable, cannot be replaced/removed, new elem cannot be added
    t = ("Norway", 4.93, 3)
    t_len = len(t)
    for item in t:
        print(item)
    print(t_len)


tuple(["This", "is", "a", "str", "list"])  # tuple constructor
bool_var = 5 in (1, 4, 9, 5, 10)
bool_var_2 = "a" not in tuple("transforms_in_char")


def minmax(items):  # returns a tuple
    return min(items), max(items)


lower, upper = minmax([2, 3, 4, 5, 3, 3, ])


def str_ex():  # str - immutable
    len_str = len("ajshdkjhdfksdhfkjshd")
    s = "New"
    s += "land"
    colors = ';'.join(['#123', '#321', '#030'])  # call join on separator
    colors.split(';')  # splits into a list
    "unforgettable".partition("forget")  # returns a tuple  ('un', 'forget' , 'able')
    "The age of {0} is {1}".format('Jim', 32)

    import math
    print("Math constants: pi={m.pi}, e={m.e}".format(m=math))


def range_ex():  # range =  arithmetic progression of integers
    range(5)
    range(0, 5)
    print(list(range(5, 10)))
    t = [6, 7, 20, 1234, 45, 123]
    for i, v in enumerate(t):
        print("i = {}, v = {}".format(i, v))


if __name__ == '__main__':
    print(minmax([1, 2, 3, 4, 6, 8, 30, 1, 0, -39]))
    range_ex()


