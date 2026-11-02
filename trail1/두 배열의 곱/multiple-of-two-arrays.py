a = [list(map(int, input().split())) for _ in range(3)]
empty = input()
b = [list(map(int, input().split())) for _ in range(3)]

answer = [[0] * 3 for _ in range(3)]

for i in range(9):
    row = (i - 1) // 3
    col = (i - 1) % 3
    answer[row][col] = a[row][col] * b[row][col]

for i in answer:
    print(*i)