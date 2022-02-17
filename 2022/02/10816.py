import sys
print = sys.stdout.write
input = sys.stdin.readline

# 가지고 있는 숫자 카드의 개수와 그 목록
N = int(input())
arr = list(map(int, input().split()))

numDic = dict()
for num in arr:
    if num in numDic:
        numDic[num] += 1
    else:
        numDic[num] = 1

# 몇 개 가지고 있는지를 구할 숫자 카드의 개수와 그 목록
M = int(input())
nums = list(map(int, input().split()))

for num in nums:
    if num in numDic:
        print(str(numDic[num]) + " ")
    else:
        print("0 ")
