import sys
input = sys.stdin.readline

if __name__ == '__main__':

    N = int(input())

    for _ in range(N):

        problem = input().strip()

        if problem == "P=NP":
            print("skipped")
        else:
            nums = list(map(int, problem.split("+")))
            print(nums[0] + nums[1])
