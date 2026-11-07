s = input().rstrip()

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]


answer = -1
x, y = 0, 0
pos = 0
p = 0
for i in s:
    if i == "F":
        x += dxs[pos]
        y += dys[pos]

        p += 1
    elif i == "R":
        pos = (pos + 5) % 4

        p += 1
    else:
        pos = (pos + 3) % 4

        p += 1

    if p and x == 0 and y == 0:
        answer = p
        break

print(answer)