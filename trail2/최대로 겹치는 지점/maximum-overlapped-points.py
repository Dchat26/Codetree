a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

amax = max(i[1] for i in alist)
answer = [0] * (amax + 1)
for x, y in alist:
    for i in range(x, y + 1):
        answer[i] += 1

print(max(answer))