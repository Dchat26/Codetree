a = int(input().rstrip())
alist = [input().split() for _ in range(a)]

amax = 0
amin = 0
temp = 0

for a, b in alist:
    a = int(a)

    if b == 'R':
        temp += a - 1
    else:
        temp -= a - 1

    amax = max(amax, temp)
    amin = min(amin, temp)

wb = [""] * (amax - amin + 1)
white = [0] * (amax - amin + 1)
black = [0] * (amax - amin + 1)

offset = -amin
p = 0

for a, b in alist:
    a = int(a)

    if b == 'R':
        for i in range(p + offset, p + offset + a):
            black[i] += 1
            wb[i] = 'B'
        p += a - 1

    else:
        for i in range(p + offset - a + 1, p + offset + 1):
            white[i] += 1
            wb[i] = 'W'
        p -= a - 1

result = [0, 0, 0]

for idx in range(len(wb)):
    if white[idx] >= 2 and black[idx] >= 2:
        result[2] += 1
    elif wb[idx] == 'W':
        result[0] += 1
    elif wb[idx] == 'B':
        result[1] += 1

print(*result)