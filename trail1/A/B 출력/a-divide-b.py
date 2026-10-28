a, b = map(int, input().split())

print(a // b, end='.')

c = (a % b) * 10
for _ in range(20):
    print(c // b, end='')

    c = (c % b) * 10