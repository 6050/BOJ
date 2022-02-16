import sys
input = sys.stdin.readline

if __name__ == '__main__':

        str = input().strip()

        while str != "#":

                cnt = 0
                for c in str:
                        if c == "a" or c == "A":
                                cnt += 1
                        elif c == "e" or c == "E":
                                cnt += 1
                        elif c == "i" or c == "I":
                                cnt += 1
                        elif c == "o" or c == "O":
                                cnt += 1
                        elif c == "u" or c == "U":
                                cnt += 1

                print(cnt)
                str = input().strip()
