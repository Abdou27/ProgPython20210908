

def begin():
    a = int(input("Donnez la valeur de a : "))
    b = int(input("Donnez la valeur de b : "))
    c = int(input("Donnez la valeur de c : "))
    d = int(input("Donnez la valeur de d : "))

    if a == c:
        print("Les droites sont parallèles")
        return

    x = (d-b)/(a-c)
    y = a*x + b

    print(x, y)


if __name__ == '__main__':
    begin()
