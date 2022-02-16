import sys

print = sys.stdout.write
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':

    M = int(input())

    S = deque([])

    for _ in range(M):
        command = input().split()
        if command[0] == "add":
            if int(command[1]) not in S:
                S.append(int(command[1]))
        elif command[0] == "remove":
            if int(command[1]) in S:
                S.remove(int(command[1]))
        elif command[0] == "check":
            if int(command[1]) in S:
                    print("1\n")
            else:
                    print("0\n")
        elif command[0] == "toggle":
            if int(command[1]) in S:
                S.remove(int(command[1]))
            else:
                S.append(int(command[1]))
        elif command[0] == "all":
                S = deque(list(range(1, 21)))
        elif command[0] == "empty":
                S = deque([])
