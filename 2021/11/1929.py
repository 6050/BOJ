if __name__ == '__main__':

    m, n = map(int, input().split())
    isPrime = [0 for i in range(1000001)]
    isPrime[1] = 1

    for i in range(2, n+1):
        for j in range(2, n+1):
            if i * j > n:
                break
            else:
                isPrime[i * j] = 1

    for i in range(m, n+1):
        if isPrime[i] == 0:
            print(i)
