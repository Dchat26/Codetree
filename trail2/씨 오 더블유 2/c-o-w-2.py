a = int(input().rstrip())
s = input().rstrip()

answer = 0
for i in range(a - 2):
    for j in range(i + 1, a - 1):
        for k in range(j + 1, a):
            if s[i] == 'C' and s[j] == 'O' and s[k] == 'W':
                answer += 1

print(answer)