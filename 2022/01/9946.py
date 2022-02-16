if __name__ == '__main__':

    word = input()

    count = 1
    while word != "END":

        word = list(word)
        bring = list(input())

        word.sort()
        bring.sort()
        
        if word == bring:
            res = "same"
        else:
            res = "different"

        print("Case " + str(count) + ":", res)

        count += 1
        word = input()
