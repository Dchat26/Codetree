n, m = map(int, input().split())
a = list(map(int, input().split()))

def can(x):
    count = 1
    cur = 0
    for v in a:
        if cur + v > x:
            count += 1
            cur = v
        else:
            cur += v
    return count <= m

lo, hi = max(a), sum(a)
while lo < hi:
    mid = (lo + hi) // 2
    if can(mid):
        hi = mid
    else:
        lo = mid + 1

print(lo)