a, b, c = input().split()
a = int(a)
b = int(b)

result = []
for _ in range(a):
    s = input().rstrip()
    if c in s and s.index(c) == 0:
        result.append(s)

print(sorted(result)[b-1])
