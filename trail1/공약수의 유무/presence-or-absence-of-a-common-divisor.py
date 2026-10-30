a, b = map(int, input().split())

is_TF = False
for i in range(a, b + 1):
    if 1920 % i == 0 and 2880 % i == 0:
        is_TF = True
        break

if is_TF:
    print(1)
else:
    print(0)
