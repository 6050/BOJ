if __name__ == '__main__':

        A, B, C = map(int, input().split())

        if A == B and B == C:
                print(10000 + A * 1000)
        elif A == B and B != C:
                print(1000 + A * 100)
        elif B == C and A != B:
                print(1000 + B * 100)
        elif A == C and A!= B:
                print(1000 + A * 100)
        elif A != B and B != C:
                print(max(A, B, C) * 100)
