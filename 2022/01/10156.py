if __name__ == '__main__':

    K, N, M = map(int, input().split())

    diff = M - K * N
    if diff > 0:
        print(0)
    else:
        print(abs(diff))
