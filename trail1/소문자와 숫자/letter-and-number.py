a = input().rstrip()

answer = ""
for i in a:
    if i.isalpha():
        answer += i.lower()
    elif i.isdigit():
        answer += i

print(answer)