a = input().rstrip()

if not '0' in a:
    a = a[:-1] + '0'
else:
    a = a[:a.index('0')] + '1' + a[a.index('0') + 1:]

print(int(a, 2))