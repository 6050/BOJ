import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

    S = input().strip()

    list = []
    for i in range(len(S)):
        list.append(S[len(S)-i-1:len(S)])

    list.sort()
    for result in list:
        print(result + "\n")
