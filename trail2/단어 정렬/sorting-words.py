a = int(input().rstrip())
alist = [input().rstrip() for _ in range(a)]

print(*(i for i in sorted(alist)), sep='\n')