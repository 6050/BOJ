import sys
input = sys.stdin.readline

if __name__ == '__main__':

    dots = []
    for _ in range(3):
        dots.append(input().split())

    dots.sort(key=lambda x:(x[0], x[1]))

    x, y = dots[0][0], dots[0][1]
    if dots[1][0] == x:
        print(dots[2][0], end=" ")
    elif dots[2][0] == x:
        print(dots[1][0], end=" ")
    else:
        print(dots[0][0], end=" ")

    if dots[1][1] == y:
        print(dots[2][1])
    elif dots[2][1] == y:
        print(dots[1][1])
    else:
        print(dots[0][1])
