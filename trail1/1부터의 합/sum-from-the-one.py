a = int(input().rstrip())

answer = 0
for i in range(1, 101):
    answer += i
    if answer >= a:
        print(i)
        break

