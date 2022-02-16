if __name__ == '__main__':

    r = 31
    M = 1234567891

    len = int(input())
    str = input()

    sigma = 0
    for i, char in enumerate(str):
        num = ord(char) - 96
        sigma += num * (r ** i)

    print(sigma % M)
