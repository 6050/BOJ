if __name__ == "__main__":

    num = ''
    for _ in range(4):
        num += input()

    ignore = 0
    if num[0] == '8' or num[0] == '9':
        if num[3] == '8' or num[3] == '9':
            if num[1] == num[2]:
                ignore = 1

    if ignore:
        print("ignore")
    else:
        print("answer")
