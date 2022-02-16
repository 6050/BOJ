import sys
input = sys.stdin.readline

if __name__ == '__main__':

    fx = input().strip().split("x")

    if fx[0] == "":
        print(1)
    elif fx[0] == "-":
        print(-1)
    elif fx[0][0] == "0" or len(fx) == 1:
        print(0)
    else:
        print(fx[0])
