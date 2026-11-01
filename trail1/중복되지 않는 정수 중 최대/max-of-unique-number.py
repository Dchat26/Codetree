a = int(input().rstrip())
alist = list(map(int, input().split()))

temp = [0] * 1001
for i in alist:
    temp[i] += 1

is_TF = True
for i in range(1000, 0, -1):
    if temp[i] == 1:
        is_TF = False
        print(i)
        break

if is_TF:
    print(-1)