import sys
print = sys.stdout.write
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())

Q = deque(list(range(1, N+1)))

ans = []
while len(Q) != 0:
    for _ in range(K-1):
        Q.append(Q.popleft())
    ans.append(Q.popleft())

print("<")
for i in range(len(ans)):
    if i == len(ans) - 1:
        print(str(ans[i]))
        break
    print(str(ans[i]) + ", ")
print(">")
