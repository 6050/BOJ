if __name__ == '__main__':

    str = input()
    while str != "0":
        if str == str[::-1]:
            print("yes")
        else:
            print("no")

        str = input()
