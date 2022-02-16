def isRightTriangle(list):
    if (list[0] ** 2 == list[1] ** 2 + list[2] ** 2
            or list[1] ** 2 == list[0] ** 2 + list[2] ** 2
            or list[2] ** 2 == list[0] ** 2 + list[1] ** 2):
        return True
    else:
        return False

if __name__ == '__main__':

    case = list(map(int, input().split()))

    while case != [0, 0, 0]:
        if isRightTriangle(case):
            print("right")
        else:
            print("wrong")
        case = list(map(int, input().split()))
