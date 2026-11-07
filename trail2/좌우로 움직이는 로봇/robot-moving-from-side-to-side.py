n, m = map(int, input().split())

t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

sec = sum(t)
result = [0] * (sec + 1)
current = 0
p = 1
for a, b in zip(t, d):
    if b == 'R':
        for _ in range(a):
            current += 1
            result[p] = current
            p += 1
    else:
        for _ in range(a):
            current -= 1
            result[p] = current
            p += 1

sec2 = sum(t_b)
result2 = [0] * (sec2 + 1)
current2 = 0
p2 = 1
for a, b in zip(t_b, d_b):
    if b == 'R':
        for _ in range(a):
            current2 += 1
            result2[p2] = current2
            p2 += 1
    else:
        for _ in range(a):
            current2 -= 1
            result2[p2] = current2
            p2 += 1

if len(result) < len(result2):
    result += [result[-1]] * (len(result2) - len(result))
else:
    result2 += [result2[-1]] * (len(result) - len(result2))

answer = 0
for i in range(1, len(result)):
    if result[i] == result2[i] and result[i-1] != result2[i-1]:
        answer += 1

print(answer)