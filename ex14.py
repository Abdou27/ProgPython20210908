import random


def echange(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def melange(arr):
    for i in range(len(arr)):
        j = random.randint(0, i)
        echange(i, j, arr)


def begin():
    arr = [random.randint(1, 10) for i in range(15)]
    print(arr)
    melange(arr)
    print(arr)


if __name__ == '__main__':
    begin()
