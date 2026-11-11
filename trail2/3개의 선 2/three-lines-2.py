a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

board = [[0] * 11 for _ in range(11)]
for x, y in alist:
    board[x][y] = 1

#가로 3
answer = 0
is_TF = False
if not is_TF:
    for i in range(9):
        for j in range(i + 1, 10):
            for k in range(j + 1, 11):
                temp = [row[:] for row in board]
                for l in range(11):
                    temp[i][l] = 0
                    temp[j][l] = 0
                    temp[k][l] = 0
        
                if sum(n for m in temp for n in m) == 0:
                    answer = 1
                    is_TF = True
                    break
    
            if is_TF:
                break
        
        if is_TF:
            break

#세로 3
if not is_TF:
    for i in range(9):
        for j in range(i + 1, 10):
            for k in range(j + 1, 11):
                temp = [row[:] for row in board]
                for l in range(11):
                    temp[l][i] = 0
                    temp[l][j] = 0
                    temp[l][k] = 0
        
                if sum(n for m in temp for n in m) == 0:
                    answer = 1
                    is_TF = True
                    break
    
            if is_TF:
                break
        
        if is_TF:
            break

#가로 세로 2 1
if not is_TF:
    for i in range(10):
        for j in range(i + 1, 11):
            for k in range(11):
                temp = [row[:] for row in board]
                for l in range(11):
                    temp[i][l] = 0
                    temp[j][l] = 0
                    temp[l][k] = 0
                
                if sum(n for m in temp for n in m) == 0:
                    answer = 1
                    is_TF = True
                    break
            
            if is_TF:
                break
        
        if is_TF:
            break
                
#가로 세로 1 2
if not is_TF:
    for i in range(10):
        for j in range(i + 1, 11):
            for k in range(11):
                temp = [row[:] for row in board]
                for l in range(11):
                    temp[l][i] = 0
                    temp[l][j] = 0
                    temp[k][l] = 0
                
                if sum(n for m in temp for n in m) == 0:
                    answer = 1
                    is_TF = True
                    break
            
            if is_TF:
                break
        
        if is_TF:
            break

print(answer)