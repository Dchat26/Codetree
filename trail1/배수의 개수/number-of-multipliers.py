a3 = 0
a5 = 0
for _ in range(10):
    a = int(input().rstrip())

    if a % 3 == 0:
        a3 += 1
        
    if a % 5 == 0:
        a5 += 1

print(a3, a5)