if __name__ == '__main__':

    l, r = map(int, input().split())

    if l != r:
        print("Odd " + str(max(l, r) * 2))
    else:
        if l != 0:
            print("Even " + str(l * 2))
        else:
            print("Not a moose")
