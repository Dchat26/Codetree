a = int(input().rstrip())
alist = [input().split() for _ in range(a)]

amax = 0
amin = 0
temp = 0

for a, b in alist:
    if b == 'R':
        temp += int(a)
    else:
        temp -= int(a)

    amax = max(amax, temp)
    amin = min(amin, temp)

answer = [0] * (amax - amin)
offset = -amin

p = 0

for a, b in alist:
    a = int(a)

    if b == 'R':
        for i in range(p + offset, p + a + offset):
            answer[i] += 1
        p += a

    else:
        for i in range(p - a + offset, p + offset):
            answer[i] += 1
        p -= a

print(sum(1 for i in answer if i >= 2))