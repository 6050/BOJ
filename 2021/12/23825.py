import sys
input = sys.stdin.readline

if __name__ == '__main__':

    N, M = list(map(int, input().split()))
    print(min(N//2, M//2))
