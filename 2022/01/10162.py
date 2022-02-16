if __name__ == '__main__':
    
	T = int(input())
	A, B, C = 0, 0, 0
    
	while True:
        
		if T >= 300:
			A += int(T / 300)
			T %= 300
		elif T >= 60:
			B += int(T / 60)
			T %= 60
		elif T >= 10:
			C += int(T/ 10)
			T %= 10
		elif T > 0 and T < 10:
			print(-1)
			break
			
		if T == 0:
		    print(A, B, C)
		    break
