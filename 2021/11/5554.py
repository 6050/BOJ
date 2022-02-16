times = []
for _ in range(4):
    times.append(int(input()))
total = sum(times)

min = total // 60
sec = total % 60

print(min)
print(int(sec))
