board = [list(map(int, input().split())) for _ in range(19)]

white = False
black = False
x, y = 0, 0
for i in range(19):
    for j in range(15):
        wc = 0
        bc = 0
        mx, my = 0, 0
        for k in range(5):
            s = board[i][j+k]

            if s == 1:
                bc += 1
            elif s == 2:
                wc += 1
            
            if k == 2:
                mx, my = i, j + k
        
        if wc == 5:
            white = True
            x, y = mx, my
        elif bc == 5:
            black = True
            x, y = mx, my

for i in range(19):
    for j in range(15):
        wc = 0
        bc = 0
        mx, my = 0, 0
        for k in range(5):
            s = board[j+k][i]

            if s == 1:
                bc += 1
            elif s == 2:
                wc += 1
            
            if k == 2:
                mx, my = j + k, i
        
        if wc == 5:
            white = True
            x, y = mx, my
        elif bc == 5:
            black = True
            x, y = mx, my
    
for i in range(15):
    for j in range(15):
        wc = 0
        bc = 0
        mx, my = 0, 0
        for k in range(5):
            s = board[i+k][j+k]

            if s == 1:
                bc += 1
            elif s == 2:
                wc += 1
            
            if k == 2:
                mx, my = i + k, j + k
        
        if wc == 5:
            white = True
            x, y = mx, my
        elif bc == 5:
            black = True
            x, y = mx, my

for i in range(18, 3, -1):
    for j in range(15):
        wc = 0
        bc = 0
        mx, my = 0, 0
        for k in range(5):
            s = board[i-k][j+k]

            if s == 1:
                bc += 1
            elif s == 2:
                wc += 1
            
            if k == 2:
                mx, my = i - k, j + k
        
        if wc == 5:
            white = True
            x, y = mx, my
        elif bc == 5:
            black = True
            x, y = mx, my

if black:
    print(1)
    print(x + 1, y + 1)
elif white:
    print(2)
    print(x + 1, y + 1)
else:
    print(0)