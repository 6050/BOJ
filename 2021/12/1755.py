import sys
print = sys.stdout.write
input = sys.stdin.readline

if __name__ == '__main__':

    M, N = map(int, input().split())

    wordDic = {"0":"zero", "1":"one", "2":"two", "3":"three", "4":"four",
               "5":"five", "6":"six", "7":"seven", "8":"eight", "9":"nine"}

    list = []
    for i in range(M, N+1):
        result = "".join(wordDic[c] for c in str(i))
        list.append([i, result])

    list.sort(key=lambda x:x[1])

    for i in range(len(list)):
        if i != 0 and i % 10 == 0:
            print("\n")
        print(str(list[i][0]) + " ")
