import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

        N, M = map(int, input().split())

        infoDic = {}
        for _ in range(N):
                info = input().split()
                infoDic[info[0]] = info[1]

        for _ in range(M):
                print(infoDic[input().strip()] + "\n")
