a = input().rstrip()

result = 0
for i in a:
    result = result * 2 + int(i)
result = result * 17

answer = ""
while result > 0:
    answer += str(result % 2)
    result //= 2

print(answer[::-1])