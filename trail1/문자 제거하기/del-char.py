a = list(input().rstrip())

while True:
    if len(a) == 1:
        break 

    b = int(input().rstrip())

    if len(a) <= b:
        a.pop(-1)
    else:
        a.pop(b)

    print("".join(a))