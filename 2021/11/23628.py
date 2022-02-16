if __name__ == '__main__':

    yearS, monthS, dayS = map(int, input().split())
    yearE, monthE, dayE = map(int, input().split())

    year = yearE - yearS

    if monthE >= monthS:
        month = monthE - monthS
    else:
        year -= 1
        month = 12 - monthS + monthE

    if dayE >= dayS:
        day = dayE - dayS
    else:
        month -= 1
        day = 30 - dayS + dayE

    if month < 0:
        year -= 1
        month += 12

    # calculate yearly leave
    yearlyLeave = 0
    i = 0
    while i < year:
        yearlyLeave += i//2 + 15
        i += 1

    # calculate monthly leave
    if month + year * 12 <= 36:
        monthlyLeave = month + year * 12
    else:
        monthlyLeave = 36

    days = str(year * 360 + month * 30 + day)

    print(yearlyLeave, monthlyLeave)
    print(days + "days")
