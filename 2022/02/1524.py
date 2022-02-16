if __name__ == '__main__':

    for _ in range(int(input())):

        tmp = input()
        N, M = map(int, input().split())
        joon = list(map(int, input().split()))
        bee = list(map(int, input().split()))

        if max(joon) >= max(bee):
            print("S")
        else:
            print("B")
