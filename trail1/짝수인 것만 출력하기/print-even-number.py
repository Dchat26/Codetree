a = int(input().rstrip())

alist = list(map(int, input().split()))

print(*[i for i in alist if i % 2 == 0])