import sys
input = sys.stdin.readline

if __name__ == '__main__':

    fx = input().strip().split("x")

    isLinear = 0
    if len(fx) == 1:
        quadratic = ""
        linear = fx[0]
        isLinear = 1
    else:
        quadratic = fx[0]
        linear = fx[1]
        isLinear = 0

    if not isLinear:
        quadratic = str(int(quadratic)/2)[:-2]

    if quadratic == "1" or quadratic == "-1":
        quadratic = quadratic[:-1]

    if linear == "1" or linear == "+1" or linear == "-1":
        linear = linear[:-1]

    if isLinear and linear == "0":
        print("W")
    elif isLinear and quadratic == "":
        print(linear + "x+W")
    elif linear == "":
        print(quadratic + "xx+W")
    else:
        print(quadratic + "xx" + linear + "x+W")
