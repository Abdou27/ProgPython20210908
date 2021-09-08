LENGTH = 254
WIDTH = 127


def calculate_new_pos(x, y, dx, dy):
    global LENGTH, WIDTH

    nx = x + dx
    if nx < 0:
        nx *= -1
    elif nx > WIDTH:
        nx = 2 * WIDTH - nx

    ny = y + dy
    if ny < 0:
        ny *= -1
    elif ny > LENGTH:
        ny = 2 * LENGTH - ny

    return nx, ny


def begin():
    x = int(input("Donnez la valeur de x : "))
    y = int(input("Donnez la valeur de y : "))
    dx = int(input("Donnez la valeur de dx : "))
    dy = int(input("Donnez la valeur de dy : "))

    print(calculate_new_pos(x, y, dx, dy))


if __name__ == '__main__':
    begin()
