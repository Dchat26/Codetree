is_TF = False
for _ in range(5):
    a = int(input().rstrip())

    if a % 3 != 0:
        is_TF = True

if is_TF:
    print(0)
else:
    print(1)