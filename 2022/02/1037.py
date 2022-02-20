if __name__ == "__main__":

    n = int(input())
    nums = list(map(int, input().split()))

    # 진짜 약수 중 가장 작은 수와 큰 수를 곱하면 됨
    print(min(nums) * max(nums))
