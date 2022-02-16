if __name__ == '__main__':

        h, m = map(int, input().split())
        need = int(input())

        m = m + need % 60
        if m >= 60:
                h += 1
                m -= 60

        if h + need // 60 >= 24:
                h -= 24

        print(h + need // 60, m)
