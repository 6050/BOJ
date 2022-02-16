if __name__ == '__main__':

    a = int(input())
    b = int(input())
    c = int(input())

    if a == 60 and a == b and b == c:
        print("Equilateral")
    elif a + b + c == 180:
        if a == b or b == c or a == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Error")
