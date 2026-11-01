a = int(input().rstrip())

answer = 0
for _ in range(a):
    if sum(map(int, input().split())) / 4 >= 60.0:
        print("pass")
        answer += 1
    else:
        print("fail")
print(answer)