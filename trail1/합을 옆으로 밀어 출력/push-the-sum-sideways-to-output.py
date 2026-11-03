a = int(input().rstrip())

result = sum(int(input().rstrip()) for _ in range(a))

print(str(result)[1:] + str(result)[0])