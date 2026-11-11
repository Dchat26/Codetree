X, Y = map(int, input().split())

answer = 0
for i in range(X, Y + 1):
    s = list(str(i))

    if len(set(s)) == 2 and (s.count(s[0]) == 1 or s.count(s[0]) == len(s) - 1):
        answer += 1

print(answer) 