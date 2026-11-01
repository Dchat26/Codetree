a = list(map(int, input().split()))

for idx, i in enumerate(a):
    if i % 3 == 0:
        print(a[idx-1])
        break