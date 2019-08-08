def sum_ex(x, y):
    print(x+y)


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)


if __name__ == '__main__':
    sum_ex(2, 3)
    sum_ex("ab", "cd")
    sum_ex([1, 2], [3, 4])
    print(fact(4))

