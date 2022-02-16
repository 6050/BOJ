if __name__ == '__main__':

    nums = input()

    if len(nums) == 2:
        print(int(nums[0]) + int(nums[1]))
    elif len(nums) == 3:
        if nums[0] == "1" and nums[1] == "0":
            print(10 + int(nums[2]))
        else:
            print(10 + int(nums[0]))
    else:
        print(20)
