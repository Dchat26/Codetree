a = list(map(int, input().split()))

max_val = 0
for i in a:
    if i > max_val:
        max_val = i

print(max_val)