if __name__ == '__main__':

    n, h, v = map(int, input().split())
    
    first = 4 * h * v
    second = 4 * (n - h) * v
    third = 4 * h * (n - v)
    fourth = 4 * (n - h) * (n - v)
    
    print(max(first, second, third, fourth))
