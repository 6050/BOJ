if __name__ == '__main__':

        first, second, marked = map(int, input().split())
        print(int((first+1)*(second+1)/(marked+1) - 1))
