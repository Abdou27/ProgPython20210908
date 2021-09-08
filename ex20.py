

def begin():
    for i in range(1, 10):
        print("Table de " + str(i) + " :")
        for j in range(1, 10):
            print("\t" + str(i) + " x " + str(j) + " = " + str(i*j))


if __name__ == '__main__':
    begin()
