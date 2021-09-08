import turtle

dist = 10


def draw_grid(n, m):
    global dist

    wn = turtle.Screen()
    wn.title("Ex 6")
    skk = turtle.Turtle()

    for i in range(n):
        for j in range(m):
            for k in range(4):
                skk.forward(dist)
                skk.right(90)
            skk.forward(dist)
        skk.right(180)
        skk.forward(dist*m)
        skk.left(90)
        skk.forward(dist)
        skk.left(90)

    turtle.done()


def begin():
    n = int(input("Donnez la valeur de n : "))
    m = int(input("Donnez la valeur de m : "))

    draw_grid(n, m)


if __name__ == '__main__':
    begin()
