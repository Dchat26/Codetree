a = input().rstrip()

answer = ""
for i in a:
    if i.isalpha():
        answer += i.upper()

print(answer)