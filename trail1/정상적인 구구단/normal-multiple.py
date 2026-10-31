a = int(input().rstrip())

for i in range(1, a + 1):
    for j in range(1, a + 1):
        print(f"{i} * {j} = {i * j}", end='')

        if j < a:
            print(",", end=' ')
    print()