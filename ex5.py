import turtle

dist = 10


def draw_stairs(n):
    global dist

    wn = turtle.Screen()
    wn.title("Ex 5")
    skk = turtle.Turtle()

    for i in range(n):
        skk.forward(dist)
        skk.right(90)
        skk.forward(dist)
        skk.left(90)

    turtle.done()


def begin():
    n = int(input("Donnez la valeur de n : "))

    draw_stairs(n)


if __name__ == '__main__':
    begin()
