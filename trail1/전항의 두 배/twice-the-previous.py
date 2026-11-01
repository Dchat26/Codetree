a, b = map(int, input().split())

p = a
pp = b
print(p, pp, end=' ')
for _ in range(8):
    p, pp = pp, 2 * p + pp

    print(pp, end=' ')