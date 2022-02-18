import sys
input = sys.stdin.readline
from collections import deque

# 모든 토마토가 익었으면 1, 아니면 0 반환
def checkAllRipe():

    count = 0
    for i in range(N):
        if 0 not in box[i]:
            count += 1
    if count == N:
        return 1
    else:
        return 0

if __name__ == "__main__":

    # 상자의 가로, 세로
    M, N = map(int, input().split())

    # 처음 상자 안 토마토의 상태 저장
    box = [[] for _ in range(N)]
    for i in range(N):
        box[i] = list(map(int, input().split()))

    if checkAllRipe() == 1:
        print(0)
        exit(0)

    # 큐 안 튜플은 (세로 위치, 가로 위치, 날짜)를 의미함
    Q = deque([])
    for i in range(N):
        for j in range(M):
            if box[i][j] == 1:
                Q.append((i, j, 0))

    while len(Q) != 0:

        r, c, d = Q.popleft()

        # 왼쪽 토마토 확인
        if c > 0 and box[r][c-1] == 0:
            box[r][c-1] = 1
            Q.append((r, c - 1, d + 1))
        # 오른쪽 토마토 확인
        if c < M - 1 and box[r][c+1] == 0:
            box[r][c+1] = 1
            Q.append((r, c + 1, d + 1))
        # 앞 토마토 확인
        if r > 0 and box[r-1][c] == 0:
            box[r-1][c] = 1
            Q.append((r - 1, c, d + 1))
        # 뒤 토마토 확인
        if r < N - 1 and box[r+1][c] == 0:
            box[r+1][c] = 1
            Q.append((r + 1, c, d + 1))

    if checkAllRipe() == 1:
        print(d)
    else:
        print(-1)
