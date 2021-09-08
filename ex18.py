import random


def pgs(e, tab):
    max = 0
    l = 0
    for i in tab:
        if i == e:
            l += 1
        else:
            if l > max:
                max = l
            l = 0

    return max


def begin():
    tab = [random.randint(1, 10) for _ in range(100)]
    print(tab)
    print(pgs(3, tab))


if __name__ == '__main__':
    begin()
