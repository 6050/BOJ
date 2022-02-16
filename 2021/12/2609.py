import sys
input = sys.stdin.readline

if __name__ == '__main__':

    A, B = map(int, input().split())
    C = A * B
    while B:
        tmp = A % B
        A = B
        B = tmp

    print(A)
    print(int(C/A))
