if __name__ == "__main__":

    count = 0

    for i in range(8):

        line = input()
        # 1, 3, 5, 7번째 줄
        if i % 2 == 0:
            for j in [0, 2, 4, 6]:
                if line[j] == 'F':
                    count += 1
        # 2, 4, 6, 8번째 줄
        else:
            for j in [1, 3, 5, 7]:
                if line[j] == 'F':
                    count += 1

    print(count)
