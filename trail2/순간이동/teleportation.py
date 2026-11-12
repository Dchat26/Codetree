a, b, x, y = map(int, input().split())

c = abs(a - b)
c2 = abs(a - x) + abs(y - b)
c3 = abs(a - y) + abs(x - b)

print(min(c, c2, c3))