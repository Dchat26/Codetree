a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

s = [0] * (max(i for _, i in alist) + 1)
for x1, x2 in alist:
    for i in range(x1, x2 + 1):
        s[i] += 1

answer = "No"
for i in s:
    if i == a:
        answer = "Yes"
        break

print(answer)