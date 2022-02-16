import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

        N = int(input())

        for _ in range(N):

                counts = [0] * 26
                string = input().strip()

                for c in string:
                        counts[ord(c) - 65] += 1

                sum = 0
                for i in range(len(counts)):
                        if counts[i] == 0:
                                sum += i + 65

                print(str(sum) + "\n")
