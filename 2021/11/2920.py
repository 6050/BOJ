def isAscending(list):
    prev = 0
    for note in list:
        if prev > note:
            return False
        prev = note

    return True

def isDescending(list):
    prev = 9
    for note in list:
        if prev < note:
            return False
        prev = note

    return True

if __name__ == '__main__':
    notes = list(map(int, input().split()))

    if isAscending(notes):
        print("ascending")
    elif isDescending(notes):
        print("descending")
    else:
        print("mixed")
