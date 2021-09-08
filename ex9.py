import math


def get_divisors(n):
    divisors = []

    for i in range(1, n+1):
        if i > math.sqrt(n):
            break

        d = n / i
        if d.is_integer():
            divisors.append(int(i))
            divisors.append(int(d))

    return divisors


def begin():
    n = int(input("Donnez la valeur de n : "))

    print(get_divisors(n))


if __name__ == '__main__':
    begin()
