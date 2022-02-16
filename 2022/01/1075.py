if __name__ == '__main__':

    N = input()
    F = int(input())

    s = "00"
    while True:
        temp = int(N[:-2] + s)
        if temp % F == 0:
            break
        if int(s) < 9:
            s = "0" + str(int(s)+1)
        else:
            s = str(int(s)+1)

    print(s)
