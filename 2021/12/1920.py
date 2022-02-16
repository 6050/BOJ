import sys
input = sys.stdin.readline

def binarySearch(list, x):
    start = 0
    end = len(list) - 1

    while start <= end:
        mid = (start + end) // 2

        if x == list[mid]:
            return 1
        elif x > list[mid]:
            start = mid + 1
        else:
            end = mid - 1

    return 0

if __name__ == '__main__':

    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    M = int(input())
    X = list(map(int, input().split()))

    for i in range(M):
        print(binarySearch(A, X[i]))
