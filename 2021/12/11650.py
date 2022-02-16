import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':

    N = int(input())

    dots = []
    for i in range(N):
        dots.append(list(map(int, input().split())))
    
    dots.sort(key=lambda x:(x[0], x[1]))

    for dot in dots:
        print(dot[0], dot[1])
