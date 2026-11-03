a = input().rstrip()
b = input().rstrip()

answer = -1
p = 0
while p < len(a):
    p += 1

    a = a[-1] + a[:-1]

    if a == b:
        answer = p
        break

print(answer)