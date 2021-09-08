import turtle


def koch(skk, n, l):
    if n == 0:
        skk.forward(l)
    else:
        koch(skk, n - 1, l / 3)
        skk.left(60)
        koch(skk, n - 1, l / 3)
        skk.right(120)
        koch(skk, n - 1, l / 3)
        skk.left(60)
        koch(skk, n - 1, l / 3)


def begin():
    n = 4
    l = 500
    wn = turtle.Screen()
    wn.setup(1000, 500)
    wn.title("Ex 23")
    skk = turtle.Turtle()
    skk.penup()
    skk.goto(-250, 0)
    skk.pendown()
    koch(skk, n, l)
    turtle.done()


if __name__ == '__main__':
    begin()
