if __name__ == "__main__":

    n = int(input())
    count, new = 0, n

    while True:

        # 주어진 수의 오른쪽 자리(일의 자리)
        right = new % 10
        # 주어진 수의 십의 자리와 일의 자리의 합
        sum = new // 10 + right

        # 새로운 수는 주어진 수의 일의 자리와 구한 합의 일의 자리를 이어 붙여서 구함
        new = right * 10 + sum % 10

        count += 1

        if new == n:
            print(count)
            break
