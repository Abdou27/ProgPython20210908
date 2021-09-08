import random


def occurences(v, t):
    return t.count(v)


def begin():
    arr = [random.randint(1, 10) for i in range(1000)]
    for i in range(1, 11):
        print(occurences(i, arr))


if __name__ == '__main__':
    begin()
