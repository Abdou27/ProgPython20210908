import turtle

dist = 10
zoom = 10


def fibonacci(n):
    f0 = 0
    f1 = 1

    if n in [0, 1]:
        return n

    t0 = f0
    t1 = f1
    t2 = None
    for i in range(2, n + 1):
        t2 = t0 + t1
        t0 = t1
        t1 = t2

    return t2


def draw_fibonacci(n):
    global dist, zoom

    wn = turtle.Screen()
    wn.title("Ex 6")
    skk = turtle.Turtle()

    for i in range(n + 1):
        fn = fibonacci(i)
        skk.circle(zoom * fn, 90)

    turtle.done()


def begin():
    n = int(input("Donnez la valeur de n : "))

    draw_fibonacci(n)


if __name__ == '__main__':
    begin()
