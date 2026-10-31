a = int(input().rstrip())

for _ in range(a):
    a, b = map(int, input().split())

    answer = 0
    for i in range(a, b + 1):
        if i % 2 == 0:
            answer += i
    
    print(answer)