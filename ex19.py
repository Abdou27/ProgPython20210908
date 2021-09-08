import random


def pgpc(tab_1, tab_2):
    min_len = min(len(tab_1), len(tab_2))
    pgpc = 0
    for i in range(min_len):
        if tab_1[i] == tab_2[i]:
            pgpc += 1
        else:
            break
    return pgpc


def begin():
    tab = [random.randint(1, 10) for _ in range(3)]
    tab_1 = [random.randint(1, 10) for _ in range(5)]
    tab_2 = [random.randint(1, 10) for _ in range(5)]
    tab_1 = tab + tab_1
    tab_2 = tab + tab_2
    print(tab_1)
    print(tab_2)
    print(pgpc(tab_1, tab_2))


if __name__ == '__main__':
    begin()
