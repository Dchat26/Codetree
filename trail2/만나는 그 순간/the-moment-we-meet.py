n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

time = sum(t)
result = [0] * (time + 1)
current = 0
p = 1
for a, b in zip(d, t):
    for _ in range(b):
        if a == 'R':
            current += 1
            result[p] = current
            p += 1
        else:
            current -= 1
            result[p] = current
            p += 1

result2 = [0] * (time + 1)
current2 = 0
p2 = 1
for a, b in zip(d2, t2):
    for _ in range(b):
        if a == 'R':
            current2 += 1
            result2[p2] = current2
            p2 += 1
        else:
            current2 -= 1
            result2[p2] = current2
            p2 += 1

answer = -1
for i in range(1, time + 1):
    if result[i] == result2[i]:
        answer = i
        break

print(answer)