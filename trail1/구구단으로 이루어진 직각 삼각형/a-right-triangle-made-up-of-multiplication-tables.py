a = int(input().rstrip())

for i in range(1, a + 1):
    for j in range(1, a - i + 2):
        print(f"{i} * {j} = {i * j}", end='')

        if j < a - i + 1:
            print(" / ", end='')
    print()