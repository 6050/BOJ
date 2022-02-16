k = int(input())
f = 25 + k * 0.01

if f < 100:
    f = 100
elif f > 2000:
    f = 2000

print("{:.2f}".format(f))
