a = int(input().rstrip())

alist = [1] * (a + 1)

for i in range(a):
    for j in range(1, a + 1):
        if i == 0:
            print("* ", end='')
        else:
            if j % 2 == 0 and alist[j] != j:
                print("* ", end='')
                alist[j] += 1
            else:
                print("  ", end='')
    print()