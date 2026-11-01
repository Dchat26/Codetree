alist = list(map(int, input().split()))

asum = 0
ac = 0
for i in alist:
    if i == 0:
        break
    elif i % 2 == 0:
        asum += i
        ac += 1

print(ac, asum)