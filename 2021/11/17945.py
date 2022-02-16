if __name__ == '__main__':

    A, B = map(int, input().split())
    X1 = int((-2 * A + (4 * A ** 2 - 4 * B) ** 0.5) / 2)
    X2 = int((-2 * A - (4 * A ** 2 - 4 * B) ** 0.5) / 2)

    if X1 == X2:
        print(X1)
    elif X1 < X2:
        print(X1, X2)
    elif X1 > X2:
        print(X2, X1)
