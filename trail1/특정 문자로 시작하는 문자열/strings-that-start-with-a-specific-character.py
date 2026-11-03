a = int(input().rstrip())
alist = [input().rstrip() for _ in range(a)]

b = input().rstrip()

acount = 0
asum = 0
for i in alist:
    if i[0] == b:
        acount += 1
        asum += len(i)

print(f"{acount} {asum / acount:.2f}")