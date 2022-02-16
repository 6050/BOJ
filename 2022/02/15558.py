from collections import deque

def BFS():

    # tuple의 첫 번째 요소는 칸(1 base), 두 번째 요소는 줄(0이 왼쪽, 1이 오른쪽)
    # 세 번째 요소는 시간
    Q = deque([(1, 0, 1)])
    visited = [[0] * (N + 1) for _ in range(2)] # 방문 여부 (1 base)

    while len(Q) != 0:

        pos, line, time = Q.popleft()
        if pos > N:
            return 1

        if visited[line][pos] == 1:
            continue

        visited[line][pos] = 1

        # 현재 있는 칸이 왼쪽 줄인 경우
        if line == 0:
            # 한 칸 앞
            if left[pos + 1] == "1":
                Q.append((pos + 1, 0, time + 1))
            # 한 칸 뒤
            if pos != 1 and pos - 1 > time and left[pos - 1] == "1":
                Q.append((pos - 1, 0, time + 1))
            # 오른쪽 줄로 k 칸 앞
            if right[pos + k] == "1":
                Q.append((pos + k, 1, time + 1))
        # 현재 있는 칸이 오른쪽 줄인 경우
        elif line == 1:
            # 한 칸 앞
            if right[pos + 1] == "1":
                Q.append((pos + 1, 1, time + 1))
            # 한 칸 뒤
            if pos != 1 and pos - 1 > time and right[pos - 1] == "1":
                Q.append((pos - 1, 1, time + 1))
            # 왼쪽 줄로 k 칸 앞
            if left[pos + k] == "1":
                Q.append((pos + k, 0, time + 1))

    return 0

if __name__ == "__main__":

    N, k = map(int, input().split())
    left = ' ' + input() + '1' * 100_000
    right = ' ' + input() + '1' * 100_000

    print(BFS())
