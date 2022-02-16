if __name__ == "__main__":

    form = input()

    alpha, num = 26, 10
    ans = 1

    for i in range(len(form)):

        if form[i] == 'c':
            if i != 0 and form[i-1] == 'c':
                ans *= alpha - 1
            else:
                ans *= alpha

        elif form[i] == 'd':
            if i != 0 and form[i-1] == 'd':
                ans *= num - 1
            else:
                ans *= num

    print(ans)
