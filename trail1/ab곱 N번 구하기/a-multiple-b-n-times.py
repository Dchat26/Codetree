a = int(input().rstrip())

for _ in range(a):
    b, c = map(int, input().split())

    prod = 1
    for i in range(b, c + 1):
        prod *= i
    
    print(prod)