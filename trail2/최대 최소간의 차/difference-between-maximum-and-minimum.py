N, K = map(int, input().split())
a = list(map(int, input().split()))

answer = float('inf')
for lo in range(1, 10001):
    hi = lo + K
    cost = 0
    for x in a:
        if x < lo:
            cost += lo - x
        elif x > hi:
            cost += x - hi
    answer = min(answer, cost)

print(answer)