import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())
    Q = deque([])

    for _ in range(N):

        command = input().split()

        if command[0] == "push":
            Q.append(command[1])
        elif command[0] == "pop":
            if len(Q) != 0:
                print(Q.popleft())
            else:
                print(-1)
        elif command[0] == "size":
            print(len(Q))
        elif command[0] == "empty":
            if len(Q) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if len(Q) != 0:
                print(Q[0])
            else:
                print(-1)
        elif command[0] == "back":
            if len(Q) != 0:
                print(Q[len(Q) - 1])
            else:
                print(-1)
