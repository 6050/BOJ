import sys

input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().split())
arr = list(map(int, input().split()))

ret = sum(arr[:M])
window = ret
last = arr[0]

for i in range(M, N):
    window -= last
    window += arr[i]
    last = arr[i - M + 1]

    ret = ret if ret > window else window

print(ret)
