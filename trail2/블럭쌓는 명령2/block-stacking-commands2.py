n, k = map(int, input().split())

nlist = [0] * (n + 1)

for _ in range(k):
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        nlist[i] += 1

print(max(nlist))