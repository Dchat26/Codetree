a = int(input().rstrip())
alist = list(map(int, input().split()))

max_val = 0
for i in range(len(alist) - 1):
    for j in range(i + 1, len(alist)):
        if alist[j] > alist[i] and max_val < alist[j] - alist[i]:
            max_val = alist[j] - alist[i]

print(max_val)