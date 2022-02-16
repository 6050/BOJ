if __name__ == '__main__':
    cnt = int(input())
    numList = list(map(int, input().split()))

    prime = 0
    for num in numList:
        notPrime = 0
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    notPrime += 1
                    break
            if notPrime == 0:
                prime += 1

    print(prime)
