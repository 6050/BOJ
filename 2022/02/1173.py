if __name__ == "__main__":

    # N: 운동하고 싶은 시간(분), m: 초기 맥박, M: 최대 맥박
    # T: 1분 운동 후 오르는 맥박, R: 1분 휴식할 때 줄어드는 맥박
    N, m, M, T, R = map(int, input().split())

    if M - m < T:
        print(-1)
    else:
        # time: 소요된 시간, p: 현재 맥박
        time, p = 0, m
        
        while N > 0:

            # 맥박이 M을 넘지 않으면 운동
            if p + T <= M:
                p += T
                N -= 1
            # 그렇지 않으면 휴식
            else:
                # 휴식 후 맥박이 최소 맥박보다 작으면 맥박이 최소 맥박이 됨
                if p - R < m:
                    p = m
                else:
                    p -= R

            time += 1

        print(time)
