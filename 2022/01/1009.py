import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

        T = int(input())
        for _ in range(T):
                a, b = map(int, input().split())
                ans = pow(a, b, 10)
                if ans:
                        print(str(ans) + "\n")
                else:
                        print("10" + "\n")
