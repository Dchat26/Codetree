a = int(input().rstrip())

alen = 0
acount = 0
for _ in range(a):
    b = input().rstrip()

    if b[0] == 'a':
        acount += 1

    alen += len(b)

print(alen, acount)