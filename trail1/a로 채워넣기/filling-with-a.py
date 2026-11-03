a = list(input().rstrip())

a[1], a[-2] = 'a', 'a'

print("".join(a))