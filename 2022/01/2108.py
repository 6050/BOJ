import sys
import math
input = sys.stdin.readline

if __name__ == '__main__':

        N = int(input())
        nums = []
        for _ in range(N):
                nums.append(int(input()))
        nums.sort()
        # 산술평균 - 소수점 이하 첫째 자리에서 반올림
        print(round(sum(nums)/N))

        # 중앙값
        print(nums[N//2])

        # 최빈값
        counts = [0] * 8001

        for i in range(N):
                if nums[i] < 0:
                        counts[abs(nums[i]) + 4000] += 1
                elif nums[i] >= 0:
                        counts[nums[i]] += 1
        maxCount = max(counts)
        # 최빈값이 여러 개면 두 번째로 작은 값 출력
        modes = []
        for i in range(len(counts)):
                if counts[i] == maxCount:
                        modes.append(i)

        for i in range(len(modes)):
                if modes[i] > 4000:
                        modes[i] -= 4000
                        modes[i] *= -1

        modes.sort()
        if len(modes) == 1:
                print(modes[0])
        else:
                print(modes[1])

        # 범위
        print(max(nums) - min(nums))
