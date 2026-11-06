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

answer = [""] * (amax - amin + 1)
offset = -amin
p = 0

for a, b in alist:
    a = int(a)

    if b == 'R':
        for i in range(p + offset, p + offset + a):
            answer[i] = "B"
        p += a - 1

    else:
        for i in range(p + offset - a + 1, p + offset + 1):
            answer[i] = "W"
        p -= a - 1

result = [0, 0]

for i in answer:
    if i == "W":
        result[0] += 1
    elif i == "B":
        result[1] += 1

print(*result)