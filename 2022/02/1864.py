if __name__ == '__main__':

    nums = {"-": 0, "\\": 1, "(": 2, "@": 3, "?": 4, ">": 5, "&": 6, "%": 7, "/": -1}

    num = input()
    while num != "#":
        res = 0
        for i in range(len(num)):
            res += nums[num[i]] * (8 ** (len(num) - i - 1))
        print(res)

        num = input()
