def Prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def Is_TF(n):
    if sum(int(i) for i in str(n)) % 2 == 0:
        return True
    return False

a, b = map(int, input().split())

answer = 0
for i in range(a, b + 1):
    if Prime(i):
        if Is_TF(i):
            answer += 1

print(answer)