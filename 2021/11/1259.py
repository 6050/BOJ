if __name__ == '__main__':

    str = input()
    while str != "0":
        if len(str) == 1:
            print("yes")

        elif len(str) == 2:
            if str[0] == str[1]:
                print("yes")
            else:
                print("no")

        elif len(str) == 3:
            if str[0] == str[2]:
                print("yes")
            else:
                print("no")

        elif len(str) == 4:
            if str[0] == str[3] and str[1] == str[2]:
                print("yes")
            else:
                print("no")

        elif len(str) == 5:
            if str[0] == str[4] and str[1] == str[3]:
                print("yes")
            else:
                print("no")

        str = input()
