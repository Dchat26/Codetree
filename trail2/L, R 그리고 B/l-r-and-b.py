board = [list(input()) for _ in range(10)]

lx, ly = 0, 0
rx, ry = 0, 0
bx, by = 0, 0
for i in range(10):
    for j in range(10):
        if board[i][j] == 'L':
            lx, ly = i, j
        
        if board[i][j] == 'R':
            rx, ry = i, j
        
        if board[i][j] == 'B':
            bx, by = i, j

dist = abs(lx-bx) + abs(ly-by) - 1
if lx == bx == rx and min(ly,by) < ry < max(ly,by): dist += 2
elif ly == by == ry and min(lx,bx) < rx < max(lx,bx): dist += 2

print(dist)