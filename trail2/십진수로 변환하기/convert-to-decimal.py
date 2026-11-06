a = input().rstrip()

answer = 0
for i in a:
    answer = answer * 2 + int(i)

print(answer)