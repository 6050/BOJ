if __name__ == '__main__':
    fiveDigits = list(map(int, input().split()))

    num = 0
    for digit in fiveDigits:
        num += digit ** 2

    print(num % 10)
