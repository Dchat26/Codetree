n = int(input().rstrip())
nlist = [list(input().rstrip()) for _ in range(n)]
a = int(input().rstrip())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dr = {"N": 0, "E": 1, "S": 2, "W": 3}

dr2 = {"N": "W", "E": "S", "S": "E", "W": "N"}
dr3 = {"N": "E", "E": "N", "S": "W", "W": "S"}

if 1 <= a <= n:
    r = "S"
    x, y = 0, a - 1

elif n + 1 <= a <= 2 * n:
    r = "W"
    x, y = a - n - 1, n - 1

elif 2 * n + 1 <= a <= 3 * n:
    r = "N"
    x, y = n - 1, 3 * n - a

else:
    r = "E"
    x, y = 4 * n - a, 0

answer = 0

while True:
    if nlist[x][y] == '\\':
        r = dr2[r]
        answer += 1
    else:
        r = dr3[r]
        answer += 1

    nx = x + dx[dr[r]]
    ny = y + dy[dr[r]]

    if 0 <= nx < n and 0 <= ny < n:
        x, y = nx, ny
    else:
        break

print(answer)