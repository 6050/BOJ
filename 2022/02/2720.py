if __name__ == "__main__":

    T = int(input())
    for _ in range(T):

        Q, D, N, P = 0, 0, 0, 0

        fee = int(input())

        Q += fee // 25
        fee %= 25

        D += fee // 10
        fee %= 10

        N += fee // 5
        fee %= 5

        P = fee

        print(Q, D, N, P)
