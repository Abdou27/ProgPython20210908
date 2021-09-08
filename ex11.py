import math


def solve(a, b, c):
    if a == 0:
        return -c/b

    delta = b*b - 4 * a * c

    if delta < 0:
        return None
    elif delta == 0:
        return -b/(2*a)
    else:
        return (-b-math.sqrt(delta))/(2*a), (-b+math.sqrt(delta))/(2*a)


def begin():
    a = int(input("Donnez la valeur de a : "))
    b = int(input("Donnez la valeur de b : "))
    c = int(input("Donnez la valeur de c : "))

    print(solve(a, b, c))


if __name__ == '__main__':
    begin()
