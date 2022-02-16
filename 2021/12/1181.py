import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())
    words = []
    for _ in range(N):
        words.append(input().strip())

    words = list(set(words))
    words.sort()
    words.sort(key=len)

    for word in words:
        print(word + "\n")
