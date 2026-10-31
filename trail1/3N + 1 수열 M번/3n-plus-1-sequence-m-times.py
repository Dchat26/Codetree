a = int(input().rstrip())

for _ in range(a):
    b = int(input().rstrip())

    answer = 0
    while b > 1:
        answer += 1

        if b % 2 == 0:
            b //= 2
        else:
            b = b * 3 + 1
    
    print(answer)