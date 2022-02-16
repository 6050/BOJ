import sys
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())

    list = []
    for i in range(N):
        list.append((i, input().split()))

    list.sort(key=lambda x:(int(x[1][0]), x[0]))

    for info in list:
        print(info[1][0], info[1][1])
