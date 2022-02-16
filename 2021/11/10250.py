if __name__ == '__main__':

    caseNum = int(input())
    caseList = []
    for i in range(caseNum):
        caseList.append(list(map(int, input().split())))

    for case in range(caseNum):

        H, W, N = caseList[case]

        rooms = []
        for i in range(1, W+1):
            for j in range(1, H+1):
                rooms.append(j*100 + i)

        print(rooms[N-1])
