if __name__ == "__main__":

    A, B, C, D = map(int, input().split())

    first = abs(abs(A-B) - abs(C-D))
    second = abs(abs(A-C) - abs(B-D))
    third = abs(abs(A-D) - abs(B-C))

    print(min(first, second, third))
