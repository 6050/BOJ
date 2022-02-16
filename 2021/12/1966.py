import sys
from collections import deque
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())

    for _ in range(N):
        count = 0

        len, index = map(int, input().split())
        Q = deque(list(map(int, input().split())))
        indexQ = deque(list(range(len)))

        while Q:

            if Q[0] == max(Q):
                count += 1
                Q.popleft()
                if indexQ.popleft() == index:
                    print(count)

            else:
                Q.append(Q.popleft())
                indexQ.append(indexQ.popleft())
