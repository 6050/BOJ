if __name__ == "__main__":

    N = int(input())
    
    # chr()은 아스키코드를 문자로 변환해주는 함수
    # 한글의 아스키코드는 44032부터 시작함
    print(chr(N+44031))
