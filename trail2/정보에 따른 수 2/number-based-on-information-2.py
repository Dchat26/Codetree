t, a, b = map(int, input().split())
s = []
n = []
for _ in range(t):
    d, i = input().split()
    i = int(i)
    if d == 'S':
        s.append(i)
    else:
        n.append(i)

answer = 0
for i in range(a, b + 1):
    sn, nn = 1001, 1001
    for j in s:
        sn = min(sn, abs(i - j))
    
    for k in n:
        nn = min(nn, abs(i - k))
    
    if sn <= nn:
        answer += 1

print(answer)