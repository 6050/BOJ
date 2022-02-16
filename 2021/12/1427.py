import sys
input = sys.stdin.readline

if __name__ == '__main__':

    N = list(input().strip())
    N.sort(reverse=True)
    
    print("".join(N))
