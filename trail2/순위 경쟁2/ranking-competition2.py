n = int(input().rstrip())
nlist = [tuple(input().split()) for _ in range(n)]

answer = 0
cur = "AB"
Ascore = 0
Bscore = 0
for a, b in nlist:
    b = int(b)

    if a == 'A':
        Ascore += b
    else:
        Bscore += b
    
    p = ""
    if Ascore == Bscore:
        p = "AB"
    elif Ascore > Bscore:
        p = "A"
    else:
        p = "B"
    
    if cur != p:
        answer += 1
        cur = p

print(answer)