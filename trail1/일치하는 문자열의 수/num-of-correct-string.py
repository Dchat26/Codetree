a, b = input().split()
a = int(a)

print(sum(1 if input().rstrip() == b else 0 for _ in range(a)))