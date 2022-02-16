import sys
input = sys.stdin.readline

if __name__ == '__main__':

        c = input().strip()
        print(ord(c) - ord("가") + 1)
