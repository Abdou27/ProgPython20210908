import random


def hamming(arr_1, arr_2):
    nbr_diff = 0
    for i in range(len(arr_1)):
        if arr_1[i] != arr_2[i]:
            nbr_diff += 1
    return nbr_diff


def begin():
    arr_1 = [random.randint(1, 10) for _ in range(100)]
    arr_2 = [random.randint(1, 10) for _ in range(100)]
    print(arr_1)
    print(arr_2)
    print(hamming(arr_1, arr_2))


if __name__ == '__main__':
    begin()
