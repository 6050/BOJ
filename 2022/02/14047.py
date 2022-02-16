if __name__ == '__main__':

    N, K = map(int, input().split())

    # 가지고 있는 동전
    coins = []
    for _ in range(N):
        coins.append(int(input()))
    coins.sort(reverse=True)

    # 동전의 개수
    count = 0
    for coin in coins:
        count += K // coin
        K -= (K // coin) * coin

    print(count)
