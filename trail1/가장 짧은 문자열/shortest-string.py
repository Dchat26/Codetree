s = set()
for _ in range(3):
    a = input().rstrip()

    s.add(len(a))

print(max(s) - min(s))