a = int(input().rstrip())

for i in range(a, 0, -1):
    for j in range(a, 0, -1):
        print(f"({i},{j})", end=' ')
    print()