a = int(input().rstrip())
alist = list(map(int, input().split()))

result = []
for idx, i in enumerate(alist, start=1):
    result.append((i, idx))

temp = sorted(result, key=lambda x: x[0])

answer = []
for a, b in result:
    for idx, c in enumerate(temp, start=1):
        a1, b1 = c
        if a == a1 and b == b1:
            answer.append(idx)
            break

print(*answer)