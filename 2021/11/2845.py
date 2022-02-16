if __name__ == '__main__':

    L, P = map(int, input().split())
    list = list(map(int, input().split()))

    people = L * P
    for article in list:
        print(article - people, end = ' ')
