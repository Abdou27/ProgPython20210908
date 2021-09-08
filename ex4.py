

def begin():
    s = int(input("Donnez la valeur de s : "))
    t = int(input("Donnez la valeur de t : "))
    n = int(input("Donnez la valeur de n : "))

    for i in range(1, n+1):
        a = s*t/100
        s += a
        print(a, s)


if __name__ == '__main__':
    begin()
