a = input().rstrip()
b = input().rstrip()

if len(a) != len(b):
    print("No")
else:
    is_TF = True
    for a, b in zip(sorted(a), sorted(b)):
        if a != b:
            is_TF = False
            break

    if is_TF:
        print("Yes")
    else:
        print("No")