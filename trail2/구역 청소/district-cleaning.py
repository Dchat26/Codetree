a, b = map(int, input().split())
c, d = map(int, input().split())

line = [0] * (max(a, b, c, d) + 1)
for i in range(a, b):
    line[i] = 1

for i in range(c, d):
    line[i] = 1

print(sum(line))