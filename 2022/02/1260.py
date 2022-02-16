from collections import deque

# 스택을 이용한 깊이 우선 탐색
def DFS():

    stack = deque([S])

    # 방문 여부 (1 base)
    visited = [0] * (N + 1)

    ans = []
    while len(stack) != 0:

        cur = stack.pop()

        # 이미 방문한 노드인 경우
        if visited[cur] == 1:
            continue

        # 처음 방문한 노드인 경우
        visited[cur] = 1
        ans.append(cur)

        # 인접한 노드를 모두 스택에 넣음
        # 숫자가 작은 노드가 스택의 위에 위치하도록 함
        for node in reversed(edges[cur]):
            stack.append(node)

    print(*ans)

# 큐를 이용한 너비 우선 탐색
def BFS():

    queue = deque([S])

    # 방문 여부 (1 base)
    visited = [0] * (N + 1)

    ans = []
    while len(queue) != 0:

        cur = queue.popleft()

        # 이미 방문한 노드인 경우
        if visited[cur] == 1:
            continue

        # 처음 방문한 노드인 경우
        visited[cur] = 1
        ans.append(cur)

        # 인접한 노드를 모두 스택에 넣음
        # 숫자가 작은 노드가 스택의 위에 위치하도록 함
        for node in edges[cur]:
            queue.append(node)

    print(*ans)

# 노드 개수, 엣지 개수, 탐색 시작 노드
N, M, S = map(int, input().split())

# 엣지 리스트 생성 (1 base)
edges = [[] for _ in range(N+1)]
for _ in range(M):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

for i in range(N + 1):
    edges[i].sort()

DFS()
BFS()
