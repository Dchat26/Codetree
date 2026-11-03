a = list(map(int, input().split()))

print(*(chr(i) for i in a), end=' ')