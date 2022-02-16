import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

        str = list(input().strip())

        for i in range(len(str)):
                if i != 0 and i % 10 == 0:
                        print("\n")
                print(str[i])
