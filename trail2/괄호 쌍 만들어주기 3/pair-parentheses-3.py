s = input().rstrip()

answer = 0
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
        if s[i] == '(' and s[j] == ')':
            answer += 1

print(answer)