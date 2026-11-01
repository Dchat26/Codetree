a = list(map(int, input().split()))

even = 0
odd = 0
for idx, i in enumerate(a):
    if idx % 2 == 0:
        odd += i
    else:
        even += i

if odd >= even:
    print(odd - even)
else:
    print(even - odd)