a = input().rstrip()

print(sum(int(i) for i in a if i.isdigit()))