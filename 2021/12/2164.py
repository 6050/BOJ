import sys
input = sys.stdin.readline
from collections import deque

if __name__ == '__main__':

    N = int(input())
    Q = deque(list(range(1, N+1)))

    while len(Q) != 1:

        Q.popleft()
        Q.append(Q.popleft())

    print(Q[0])
