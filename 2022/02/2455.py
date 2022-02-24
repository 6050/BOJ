if __name__ == "__main__":

    people, max = 0, -1
    for i in range(4):
        getOff, getOn = map(int, input().split())
        people += getOn - getOff
        if people > max:
            max = people

    print(max)
