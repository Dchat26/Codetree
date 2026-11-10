n, k = map(int, input().split())
nlist = [tuple(input().split()) for _ in range(n)]

s = max(int(i) for i, _ in nlist)

line = [0] * (s + 1)

for a, b in nlist:
    a = int(a)

    if b == 'G':
        line[a] = 1
    else:
        line[a] = 2

size = min(k + 1, s + 1)

temp = sum(line[:size])
answer = temp
for i in range(1, s - size + 2):
    temp -= line[i - 1]
    temp += line[i + size - 1]

    answer = max(answer, temp)

print(answer)