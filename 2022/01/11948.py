if __name__ == '__main__':

    sc = []
    for _ in range(4):
        sc.append(int(input()))
    sc.sort()
    
    print(sum(sc[1:]) + max(int(input()), int(input())))
