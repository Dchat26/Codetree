n, m = map(int, input().split())
ns = input().rstrip()

p = n
for _ in range(m):
    a = input().split()

    if len(a) == 1:
        if a[0] == 'L':
            if p > 0:
                p -= 1
        elif a[0] == 'R':
            if p < len(ns):
                p += 1
        else:
            if p < len(ns):
                ns = ns[:p] + ns[p+1:]
    else:
        s = a[1]
        ns = ns[:p] + s + ns[p:]
        p += 1

print(ns)