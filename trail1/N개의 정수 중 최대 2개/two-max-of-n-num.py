import sys

a = int(input().rstrip())

alist = list(map(int, input().split()))

a1 = alist[0]
a2 = -sys.maxsize
for i in alist[1:]:
    if i >= a1:
        a2 = a1
        a1 = i
    elif a2 <= i:
        a2 = i

print(a1, a2)