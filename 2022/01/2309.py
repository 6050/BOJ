import sys
input = sys.stdin.readline

if __name__ == '__main__':

        heights = [0]
        for _ in range(9):
                heights.append(int(input()))
        heights.sort()

        fake1, fake2 = 0, 0
        for i in range(1, 10):
                for j in range(1, 10):
                        if j != i:
                                totalHeight = sum(heights) - heights[i] - heights[j]
                                if totalHeight == 100:
                                        fake1 = i
                                        fake2 = j
                                        break

        for dwarf in range(1, 10):
                if dwarf != fake1 and dwarf != fake2:
                        print(heights[dwarf])
