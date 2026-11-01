a = int(input().rstrip())

alist = list(map(int, input().split()))

print(*[i * i for i in alist])