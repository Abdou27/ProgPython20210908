
def fibonacci(n):
    f0 = 0
    f1 = 1

    if n == 1:
        return 1

    t0 = f0
    t1 = f1
    t2 = None
    for i in range(2, n+1):
        t2 = t0 + t1
        t0 = t1
        t1 = t2

    return t2


def begin():
    n = int(input("Donnez la valeur de n : "))

    print(fibonacci(n))


if __name__ == '__main__':
    begin()
