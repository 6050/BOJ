if __name__ == '__main__':

    N = int(input())

    meetings = []
    for _ in range(N):
        meetings.append(list(map(int, input().split())))
    meetings.sort(key = lambda x: (x[1], x[0]))

    count , endTime = 0, 0
    for start, end in meetings:
        if start >= endTime:
            count += 1
            endTime = end

    print(count)
