import random


def sous_mot(a, b, tab):
    found_a = False
    found_both_in_order = False

    for i in tab:
        if i == a:
            found_a = True
        elif i == b and found_a:
            found_both_in_order = True
            break

    return found_both_in_order


def begin():
    tab = [random.randint(1, 10) for _ in range(10)]
    print(tab)
    print(sous_mot(1, 3, tab))


if __name__ == '__main__':
    begin()
