def is_TF(n):
    return n % 3 == 0 or any(i in str(n) for i in ('3', '6', '9'))


a, b = map(int, input().split())

answer = 0
for i in range(a, b + 1):
    if is_TF(i):
        answer += 1

print(answer)