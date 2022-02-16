import time

if __name__ == '__main__':
    print(time.strftime("%Y\n%m\n%d", time.localtime(time.time() - 32400)))
