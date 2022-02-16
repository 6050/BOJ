num = int(input())
current = int(input())

total = 0
for i in range(num):
    next = int(input())

    if next >= current:
        bigger = next
        smaller = current
    else:
        bigger = current
        smaller = next

    angle1 = 360 - bigger + smaller
    angle2 = bigger - smaller

    if angle1 >= angle2:
        total += angle2
    else:
        total += angle1

    current = next

print(total)
