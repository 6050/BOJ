from collections import deque

if __name__ == '__main__':

    list = deque([])
    cnt = int(input())
    for _ in range(cnt):
        num = int(input())
        if num != 0:
            list.append(num)
        if num == 0:
            list.pop()

    print(sum(list))
