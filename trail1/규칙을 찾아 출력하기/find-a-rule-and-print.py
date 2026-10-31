a = int(input().rstrip())

for i in range(a):
    for j in range(a):
        if i == 0:
            print('* ', end='')
        else:
            if i > j:
                print("* ", end='')
            elif j == a - 1:
                print("* ", end='')
            else:
                print("  ", end='')
    print()