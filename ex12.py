
def occurences(v, t):
    return t.count(v)


def begin():
    print(occurences(2, [1, 2, 2, 3, 5, 6, 2, 4, 10]))


if __name__ == '__main__':
    begin()
