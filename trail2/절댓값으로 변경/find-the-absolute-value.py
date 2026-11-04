def p(alist):
    for idx, i in enumerate(alist):
        if i < 0:
            alist[idx] = -i
            

a = int(input().rstrip())
alist = list(map(int, input().split()))

p(alist)

print(*alist)