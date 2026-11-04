def change(n):
    for idx, i in enumerate(n):
        if i % 2 == 0:
            n[idx] //= 2


a = int(input().rstrip())

alist = list(map(int, input().split()))

change(alist)

print(*alist)