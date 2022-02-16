if __name__ == '__main__':
    
    X, Y = map(int, input().split())
    min = 1000 / Y * X
	
    N = int(input())
	
    for _ in range(N):
        x, y = map(int, input().split())
        price = 1000 / y * x
        if price < min:
            min = price
            
    print(min)
