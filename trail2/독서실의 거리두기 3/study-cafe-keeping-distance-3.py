a = int(input().rstrip())
s = input().rstrip()

one = [i for i in range(a) if s[i] == '1']
dist = [one[i+1] - one[i] for i in range(len(one) - 1)]

p = max(dist) // 2
for i in dist:
    p = min(p, i)

print(p)