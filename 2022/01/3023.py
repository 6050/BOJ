import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

        R, C = map(int, input().split())
        card = []

        # 좌상단
        for i in range(R):
                card.append(list(input().strip()))

        A, B = map(int, input().split())

        # 우상단
        for i in range(R):
                for j in range(C, 2 * C):
                        card[i].append(card[i][2 * C - j - 1])

        # 좌하단
        for i in range(R, 2 *R):
                card.append([])
                for j in range(C):
                        card[i].append(card[2 * R - i - 1][j])

        # 우하단
        for i in range(R, 2 * R):
                for j in range(C, 2 * C):
                        card[i].append(card[2 * R - i - 1][2 * C - j - 1])

        if card[A-1][B-1] == ".":
                card[A-1][B-1] = "#"
        else:
                card[A-1][B-1] = "."

        for r in range(2 * R):
                for c in card[r]:
                        print(c)
                print("\n")
