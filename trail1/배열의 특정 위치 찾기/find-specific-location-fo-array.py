alist = list(map(int, input().split()))

a1, b1, b2 = 0, 0, 0
for idx, i in enumerate(alist):
    if idx % 2 == 1:
        a1 += i
    
    if (idx + 1) % 3 == 0:
        b1 += i
        b2 += 1

print(f"{a1} {b1 / b2:.1f}")