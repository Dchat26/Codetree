import sys

a = int(input().rstrip())
alist = [tuple(map(int, input().split())) for _ in range(a)]

if len(set(alist)) == 1:
    print(0)
else:
    answer = sys.maxsize
    for x, y in alist:
        mx, nx = -sys.maxsize, sys.maxsize
        my, ny = -sys.maxsize, sys.maxsize
        for x2, y2 in alist:
            if x == x2 and y == y2:
                continue
        
            mx = max(mx, x2)
            nx = min(nx, x2)
            my = max(my, y2)
            ny = min(ny, y2)

        answer = min(answer, (mx - nx) * (my - ny))

    print(answer)