a = input().rstrip()
b = input().rstrip()

answer = 0
for i in range(len(a) - 1):
    s = a[i] + a[i+1]
    if s == b:
        answer += 1

print(answer)