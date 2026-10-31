a, b = map(int, input().split())

result = [i for i in range(b, a - 1, -1) if i % 2 == 0]

for i in range(1, 10):
    for idx, j in enumerate(result):
        print(f"{j} * {i} = {j * i}", end='')

        if idx + 1 < len(result):
            print(" / ", end='')
    print()