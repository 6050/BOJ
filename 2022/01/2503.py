if __name__ == '__main__':

        answers = []
        for i in range(123, 988):
                num = str(i)
                if num[0] == num[1] or num[1] == num[2] or num[0] == num[2] or "0" in num:
                        continue
                else:
                        answers.append(i)

        N = int(input())
        for _ in range(N):

                guess, inputS, inputB = map(int, input().split())
                guess = str(guess)

                temp = []
                for i in range(len(answers)):
                        strike, ball = 0, 0
                        possible = str(answers[i])
                        for j in range(3):
                                if possible[j] == guess[j]:
                                       strike += 1
                                elif possible[j] != guess[j] and possible[j] in guess:
                                        ball += 1

                        if inputS != strike or inputB != ball:
                                continue
                        else:
                                temp.append(answers[i])
                answers = temp

        print(len(answers))
