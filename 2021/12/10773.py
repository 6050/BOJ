import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':

    list = deque([])
    cnt = int(input())
    for _ in range(cnt):
        num = int(input())
        if num != 0:
            list.append(num)
        else:
            list.pop()

    print(sum(list))
