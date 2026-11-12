a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

line = [0] * (max(i for _, i in alist) + 1)
for x1, x2 in alist:
    for i in range(x1, x2 + 1):
        line[i] += 1

answer = "No"
for i in line:
    if i == a - 1:
        answer = "Yes"
        break

print(answer)