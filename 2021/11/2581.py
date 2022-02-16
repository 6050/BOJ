if __name__ == '__main__':

    m, n = int(input()), int(input())
    primeList = []

    for num in range(m, n+1):
        divisible = 0
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    divisible += 1
                    break
            if divisible == 0:
                primeList.append(num)

    if len(primeList) == 0:
        print(-1)
    else:
        print(sum(primeList))
        print(primeList[0])
