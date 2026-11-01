answer = [0] * 4
for _ in range(3):
    a, b = input().split()
    b = int(b)

    if b >= 37:
        if a == 'Y':
            answer[0] += 1
        else:
            answer[1] += 1
    else:
        if a == 'Y':
            answer[2] += 1
        else:
            answer[3] += 1

print(*answer, end=' ')

if answer[0] >= 2:
    print('E')