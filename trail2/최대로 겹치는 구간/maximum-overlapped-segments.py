a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

amin = min(i[0] for i in alist)
amax = max(i[1] for i in alist)

answer = [0] * (amax - amin + 2)
offset = 0
if amin < 0:
    offset = -amin

for x, y in alist:
    for i in range(x + offset, y + offset):
        answer[i] += 1

print(max(answer))