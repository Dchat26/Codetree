from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True
q = deque([1])
answer = 0

while q:
    cur = q.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            answer += 1
            q.append(nxt)

print(answer)