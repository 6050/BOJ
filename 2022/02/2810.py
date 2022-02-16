if __name__ == '__main__':

    N = int(input())
    seats = input()

    count, holder = 0, 1
    while count < len(seats):
        if seats[count] == "S":
            holder += 1
        elif seats[count] == "L":
            count += 1
            holder += 1
        count += 1

    if holder > N:
        print(N)
    else:
        print(holder)
