a = [input().rstrip() for _ in range(10)]

b = input().rstrip()

is_TF = True
for i in a:
    if i[-1] == b:
        print(i)
        is_TF = False

if is_TF:
    print("None")