if __name__ == '__main__':

        N = int(input())
        nums = []
        for _ in range(N):
                nums.append(int(input()))
        nums.sort()
        for num in nums:
                print(num)
