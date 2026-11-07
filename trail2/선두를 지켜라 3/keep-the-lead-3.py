N, M = map(int, input().split())

v = []
t = []
for _ in range(N):
    vi, ti = map(int, input().split())
    v.append(vi)
    t.append(ti)

v2 = []
t2 = []
for _ in range(M):
    vi, ti = map(int, input().split())
    v2.append(vi)
    t2.append(ti)

hour = sum(t)

result = [0] * (hour + 1)
current = 0
p = 1
for a, b in zip(v, t):
    for _ in range(b):
        current += a
        result[p] = current
        p += 1

result2 = [0] * (hour + 1)
current2 = 0
p2 = 1
for a, b in zip(v2, t2):
    for _ in range(b):
        current2 += a
        result2[p2] = current2
        p2 += 1

result3 = []
for a, b in zip(result, result2):
    if a > b:
        result3.append(1)
    elif a < b:
        result3.append(2)
    else:
        result3.append(3)

answer = 0
for i in range(len(result3) - 1):
    if result3[i] != result3[i+1]:
        answer += 1

print(answer)