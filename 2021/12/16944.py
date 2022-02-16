import sys
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())
    password = list(input().strip())

    big, small, num, special, need = 0, 0, 0, 0, 0
    for c in password:
        code = ord(c)
        if ord(c) in range(65, 91):
            big += 1
        elif ord(c) in range(97, 123):
            small += 1
        elif ord(c) in range(48, 58):
            num += 1
        elif c in list("!@#$%^&*()-+"):
            special += 1

    if big == 0:
        need += 1
    if small == 0:
        need += 1
    if num == 0:
        need += 1
    if special == 0:
        need += 1
    if N + need < 6:
        need += 6 - N - need

    print(need)
