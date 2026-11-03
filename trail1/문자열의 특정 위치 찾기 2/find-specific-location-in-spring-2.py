a = input().rstrip()

alist = ["apple", "banana", "grape", "blueberry", "orange"]

answer = 0
for i in alist:
    for j in range(2, 4):
        if i[j] == a:
            print(i)
            answer += 1
            break
print(answer)