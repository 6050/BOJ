import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':

    num = int(input())

    for _ in range(num):
        stack = deque([])
        PS = list(input().strip())
        result = 1

        for p in PS:
            if p == "(":
                stack.append(p)
            else:
                if len(stack) == 0:
                    result = 0
                    break
                else:
                    stack.pop()

        if result == 1 and len(stack) == 0:
            print("YES")
        else:
            print("NO")
