a = [input().rstrip() for _ in range(3)]

lines = []

for i in range(3):
    lines.append(a[i])

for j in range(3):
    lines.append(''.join(a[i][j] for i in range(3)))

lines.append(''.join(a[i][i] for i in range(3)))
lines.append(''.join(a[i][2-i] for i in range(3)))

answer = set()
for i in lines:
    if len(set(i)) == 2:
        answer.add(frozenset(i))

print(len(answer))