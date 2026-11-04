def is_TF(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


a, b = map(int, input().split())

answer = 0
for i in range(a, b + 1):
    if i == 2:
        answer += 2
    elif is_TF(i):
        answer += i

print(answer)