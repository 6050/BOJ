if __name__ == '__main__':

    nums = []
    count = 0
    while len(nums)< 1000:
        for i in range(count):
            nums.append(count)
        count += 1

    A, B = map(int, input().split())
    print(sum(nums[A-1:B]))
