import sys
from itertools import combinations

n = int(input().rstrip())
nlist = [tuple(map(int, input().split())) for _ in range(n)]
s = max(i for _, i in nlist)

answer = -sys.maxsize
for a, b in nlist:
    board = [0] * (s + 1)
    for a2, b2 in nlist:
        if a == a2 and b == b2:
            continue
        
        for i in range(a2, b2):
            board[i] = 1
    
    answer = max(answer, sum(board))

print(answer)