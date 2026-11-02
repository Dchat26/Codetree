a, b = map(int, input().split())

alist = [list(map(int, input().split())) for _ in range(a)]
blist = [list(map(int, input().split())) for _ in range(a)]

answer = [[0] * b for _ in range(a)]

for i in range(a * b + 1):
    row = (i - 1) // b
    col = (i - 1) % b
    if alist[row][col] == blist[row][col]:
        answer[row][col] = 0
    else:
        answer[row][col] = 1

for i in answer:
    print(*i)