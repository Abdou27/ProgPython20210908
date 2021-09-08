import random


def max_min(arr):
    _max = 0
    for sub_arr in arr:
        _min = min(sub_arr)
        if _min > _max:
            _max = _min
    return _max


def begin():
    tab = [[random.randint(1, 10) for _ in range(5)] for _ in range(10)]
    print(tab)
    print(max_min(tab))


if __name__ == '__main__':
    begin()
