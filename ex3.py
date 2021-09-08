
def begin():
    n = int(input("Donnez la valeur de n : "))

    arr = [i for i in range(1, n+ 1)]
    sum_arr = sum(arr)

    print(sum_arr)
    print(sum_arr == (n * (n + 1) / 2))


if __name__ == '__main__':
    begin()
