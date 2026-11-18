from collections import deque

n = int(input().rstrip())
visited = [False] * n * 2
nlist = [0] * n * 2

visited[n] = True
q = deque([n])
answer = 0
while q:
    p = q.popleft()
    if p == 1:
        answer = nlist[p]
        break
    
    if not visited[p-1]:
        visited[p-1] = True
        nlist[p-1] = nlist[p] + 1
        q.append(p - 1)

    if not visited[p+1]:
        visited[p+1] = True
        nlist[p+1] = nlist[p] + 1
        q.append(p + 1) 

    if p % 2 == 0 and not visited[p // 2]:
        visited[p // 2] = True
        nlist[p // 2] = nlist[p] + 1
        q.append(p // 2)
    
    if p % 3 == 0 and not visited[p // 3]:
        visited[p // 3] = True
        nlist[p // 3] = nlist[p] + 1
        q.append(p // 3)

print(answer)