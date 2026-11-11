a, b = map(int, input().split())
alist = [tuple(map(int, input().split())) for _ in range(a)]

answer = 0
for i in range(a):
    temp = [(p + s) for p, s in alist]
    temp[i] = (alist[i][0] // 2 + alist[i][1])
    temp.sort()

    total = 0
    count = 0
    for cost in temp:
        if total + cost > b:
            break

        total += cost
        count += 1

    answer = max(answer, count)

print(answer)