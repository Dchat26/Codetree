a = int(input().rstrip())

for i in range(a, 0, -1):
    print(" ".join('*' * i))