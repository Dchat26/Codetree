import sys

a = int(input().rstrip())
alist = []
xset = set()
yset = set()
for _ in range(a):
    x, y = map(int, input().split())

    xset.add(x)
    yset.add(y)
    alist.append((x, y))

answer = sys.maxsize
for i in range(1, 101):
    for j in range(1, 101):
        if not i in xset and not j in yset:
            a, b, c, d = 0, 0, 0, 0
            for x, y in alist:
                if x < i and y < j:
                    a += 1
                elif x < i and y > j:
                    b += 1
                elif x > i and y > j:
                    c += 1
                else:
                    d += 1
            
            answer = min(answer, max(a, b, c, d))

print(answer)