def div(n):
    return sum(i for i in range(1, n + 1)) // 10

a = int(input().rstrip())

answer = div(a)

print(answer)