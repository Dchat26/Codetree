a, b = map(int, input().split())

alist = list(map(int, input().split()))

for _ in range(b):
    c = input().split()

    if len(c) == 2:
        d, e = map(int, c)

        if d == 1:
            print(alist[e-1])
        elif d == 2:
            if e in alist:
                print(alist.index(e) + 1)
            else:
                print(0)
    else:
        d, e, f = map(int, c)

        if d == 3:
            print(*[alist[i-1] for i in range(e, f + 1)])