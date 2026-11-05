a = int(input().rstrip())
alist = list(map(int, input().split()))

alist.sort()
print(*alist)
print(*alist[::-1])