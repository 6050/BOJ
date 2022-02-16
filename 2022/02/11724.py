import sys
input = sys.stdin.readline
from collections import deque

def BFS():

    Q = deque([1])

    visited = [0] * (node + 1)

    CC = 0
    while True:

        if len(Q) != 0:
            cur = Q.popleft()
        else:
            if sum(visited) == node + 1:
                break
            else:
                CC += 1
                cur = visited.index(0)

        if visited[cur] == 1:
            continue

        visited[cur] = 1
        for i in edges[cur]:
            Q.append(i)

    print(CC)

if __name__ == "__main__":

    node, edge = map(int, input().split())
    edges = [[] for _ in range(node + 1)]

    for _ in range(edge):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    BFS()
