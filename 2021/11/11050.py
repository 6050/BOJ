if __name__ == '__main__':

    N, K = map(int, input().split())

    if K < 0 or K > N:
        print(0)
    else:
        nFactorial, kFactorial, diffFactorial = 1, 1, 1
        for i in range(2, N+1):
            nFactorial *= i
        for i in range(2, K+1):
            kFactorial *= i
        for i in range(2, N-K+1):
            diffFactorial *= i

        print(int(nFactorial / (kFactorial * diffFactorial)))
