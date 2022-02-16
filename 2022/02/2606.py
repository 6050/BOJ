from collections import deque

def DFS():

    stack = deque([1])

    visited = [0] * (com + 1)

    linked = []
    while len(stack) != 0:

        cur = stack.pop()

        if visited[cur] == 1:
            continue

        visited[cur] = 1
        linked.append(cur)

        for i in lines[cur]:
            stack.append(i)

    print(len(linked) - 1)

if __name__ == "__main__":

    # 노드 개수, 엣지 개수, 탐색 시작 노드
    com = int(input())
    line = int(input())

    # 엣지 리스트 생성 (1 base)
    lines = [[] for _ in range(com+1)]
    for _ in range(line):
        start, end = map(int, input().split())
        lines[start].append(end)
        lines[end].append(start)

    for i in range(com + 1):
        lines[i].sort()

    DFS()
