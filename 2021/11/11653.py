if __name__ == '__main__':

    n = int(input())
    dividerList = []

    divider = 2
    while True:
        for divider in range(2, n):
            if n % divider == 0:
                n = int(n/divider)
                dividerList.append(divider)
                break
        if divider >= n-1:
            break
    dividerList.append(n)

    if n != 1:
        for num in dividerList:
            print(num)
