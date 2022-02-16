if __name__ == '__main__':

        A = int(input())
        B = int(input())
        C = int(input())
        D = int(input())
        E = int(input())

        time = 0

        while A < 0:
            time += C
            A += 1

        if A == 0:
            time += D

        while A < B:
            time += E
            A += 1

        print(time)
