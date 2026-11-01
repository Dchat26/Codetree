a = int(input().rstrip())
alist = list(map(int, input().split()))

p = 0
for idx, i in enumerate(alist):
    if i == 2:
        p += 1
    
    if p == 3:
        print(idx + 1)
        break