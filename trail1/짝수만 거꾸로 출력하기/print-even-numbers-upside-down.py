a = int(input().rstrip())

alist = list(map(int, input().split()))

print(*[i for i in alist[::-1] if i % 2 == 0])