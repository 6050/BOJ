if __name__ == '__main__':
    x, y, w, h = map(int, input().split())

    diffW = w - x
    diffH = h - y
    dist = ( (diffW) ** 2 + (diffH) ** 2) ** 0.5

    distList = [x, y, diffW, diffH]
    distList.sort()

    print(distList[0])
