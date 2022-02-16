if __name__ == '__main__':

        X, Y = map(list, input().split())
        revX, revY = X, Y
        revX.reverse()
        revY.reverse()
        sum = list(str(int("".join(revX)) + int("".join(revY))))
        sum.reverse()

        print(int("".join(sum)))
