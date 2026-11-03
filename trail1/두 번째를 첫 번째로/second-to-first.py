a = list(input().rstrip())

first = a[0]
second = a[1]

for idx, i in enumerate(a):
    if i == second:
        a[idx] = first

print("".join(a))