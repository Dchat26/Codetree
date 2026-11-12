N = int(input())
heights = [int(input()) for _ in range(N)]

answer = float('inf')
for lo in range(0, 101):
    hi = lo + 17
    cost = 0
    for h in heights:
        if h < lo:
            cost += (lo - h) ** 2
        elif h > hi:
            cost += (h - hi) ** 2
    answer = min(answer, cost)

print(answer)