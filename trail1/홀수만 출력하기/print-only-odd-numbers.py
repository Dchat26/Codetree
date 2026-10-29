a = int(input().rstrip())

for _ in range(a):
    b = int(input().rstrip())

    if b % 2 == 1 and b % 3 == 0:
        print(b)