if __name__ == '__main__':

    ca, ba, pa = map(int, input().split())
    cr, br, pr = map(int, input().split())
    
    res = 0
    if cr - ca > 0:
        res += cr - ca
    if br - ba > 0:
        res += br - ba
    if pr - pa > 0:
        res += pr - pa
        
    print(res)
