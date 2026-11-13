N = int(input())
segs = [tuple(map(int, input().split())) for _ in range(N)]

ans = float('inf')
for i in range(N):
    rest = segs[:i] + segs[i+1:]
    lo = min(s[0] for s in rest)
    hi = max(s[1] for s in rest)
    ans = min(ans, hi - lo)

print(ans)