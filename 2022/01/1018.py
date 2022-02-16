import sys
input = sys.stdin.readline

if __name__ == '__main__':


        N, M = map(int, input().split())
        board = []
        for _ in range(N):
                board.append(input().strip())

        counts = []
        for i in range(N - 7):
                for j in range(M - 7):
                        count1, count2 = 0, 0
                        for r in range(i, i + 8):
                                for c in range(j, j + 8):
                                        if (r+c) % 2 == 0:
                                                if board[r][c] != "W":
                                                        count1 += 1
                                                if board[r][c] != "B":
                                                        count2 += 1
                                        else:
                                                if board[r][c] != "B":
                                                        count1 += 1
                                                if board[r][c] != "W":
                                                        count2 += 1
                        counts.append(min(count1, count2))

        print(min(counts))
