if __name__ == '__main__':

    apple = 3 * int(input()) + 2 * int(input()) + int(input())
    banana = 3 * int(input()) + 2 * int(input()) + int(input())
    
    if apple > banana:
        print("A")
    elif banana > apple:
        print("B")
    else:
        print("T")
