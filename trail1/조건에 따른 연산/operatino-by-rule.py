a = int(input().rstrip())

cnt = 0
while a < 1000:
    cnt += 1
    
    if a % 2 == 0:
        a = a * 3 + 1
    else:
        a = a * 2 + 2

print(cnt)