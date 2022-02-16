if __name__ == '__main__':

    str = input()

    if len(str) < 5:
        print("not cute")
    elif str[-5:] == "driip":
        print("cute")
    else:
        print("not cute")
