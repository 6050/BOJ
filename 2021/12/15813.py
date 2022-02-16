import sys
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())
    name = list(input().strip())

    score = 0
    for c in name:
        score += ord(c) - 64

    print(score)
