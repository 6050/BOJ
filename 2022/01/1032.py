import sys
input = sys.stdin.readline

if __name__ == '__main__':

        N = int(input())

        pattern = list(input().strip())

        for _ in range(N-1):
                new = list(input().strip())
                for i in range(len(pattern)):
                        if new[i] != pattern[i]:
                                pattern[i] = "?"

        print("".join(pattern))
