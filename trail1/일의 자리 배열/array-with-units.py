a, b = map(int, input().split())

print(a, b, end=' ')
p = a
pp = b
for _ in range(8):
    p, pp = pp, (p + pp) % 10
    print(pp, end=' ')