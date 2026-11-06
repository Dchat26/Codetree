a, b = map(int, input().split())

answer = ""
while a > 0:
    answer += str(a % b)
    a //= b

print(answer[::-1])