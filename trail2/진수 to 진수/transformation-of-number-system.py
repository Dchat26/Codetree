a, b = map(int, input().split())
n = input().rstrip()

if n == '0':
    print(0)
else:
    result = 0
    for i in n:
        result = result * a + int(i)

    answer = ""
    while result > 0:
        answer += str(result % b)
        result //= b

    print(answer[::-1])