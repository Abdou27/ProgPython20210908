hanoi = {}


def solve_hanoi(n, s, d, t):
    global hanoi
    if n != 0:
        solve_hanoi(n-1, s, t, d)
        to_move = min(hanoi[s])
        print("Move " + str(to_move) + " on " + str(d))
        hanoi[s].remove(to_move)
        hanoi[d].append(to_move)
        solve_hanoi(n-1, t, d, s)


def construct_hanoi(n):
    global hanoi

    t1 = [i for i in range(1, n+1)]
    t1.reverse()
    t2 = []
    t3 = []

    hanoi[1] = t1
    hanoi[2] = t2
    hanoi[3] = t3


def begin():
    n = 5
    construct_hanoi(n)
    print(hanoi)
    solve_hanoi(n, 1, 3, 2)
    print(hanoi)


if __name__ == '__main__':
    begin()
