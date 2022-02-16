import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':

    num = int(input())

    deque = deque([])
    for _ in range(num):
        command = input().split()

        if command[0] == "push_front":
            deque.appendleft(int(command[1]))
        elif command[0] == "push_back":
            deque.append(int(command[1]))
        elif command[0] == "pop_front":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.popleft())
        elif command[0] == "pop_back":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque.pop())
        elif command[0] == "size":
            print(len(deque))
        elif command[0] == "empty":
            if len(deque) == 0:
                print(1)
            else:
                print(0)
        elif command[0] == "front":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[0])
        elif command[0] == "back":
            if len(deque) == 0:
                print(-1)
            else:
                print(deque[len(deque)-1])
