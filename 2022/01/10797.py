if __name__ == '__main__':

        day = int(input())

        count = 0
        for car in list(map(int, input().split())):
                if car == day:
                        count += 1

        print(count)
