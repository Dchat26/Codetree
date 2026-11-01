a = int(input().rstrip())
alist = list(map(int, input().split()))

min_val = 100
alen = len(alist)
for i in range(alen - 1):
    for j in range(i + 1, alen):
        result = alist[j] - alist[i]
        if result < min_val:
            min_val = result

print(min_val)