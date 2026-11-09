s = input().rstrip()

answer = 0
for i in range(len(s) - 1):
    for j in range(len(s) - 1, 0, -1):
        if s[i] == s[i+1] == '(' and s[j] == s[j-1] == ')' and i + 2 <= j:
            answer +=1

print(answer)