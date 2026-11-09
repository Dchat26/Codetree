N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]

directions = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (1, -1), (-1, 1), (1, 1)]

answer = 0
for i in range(N):
    for j in range(M):
        for dx, dy in directions:
            temp = ""
            for k in range(3):
                px, py = i + dx * k, j + dy * k

                if 0 <= px < N and 0 <= py < M:
                    temp += arr[px][py]
            
            if temp == "LEE":
                answer += 1

print(answer)