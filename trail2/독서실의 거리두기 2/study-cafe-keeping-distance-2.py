N = int(input())
seats = input().rstrip()

s = [i for i in range(N) if seats[i] == '1']
dist = [s[i+1] - s[i] for i in range(len(s) - 1)]


D = min(dist) if dist else N

result = []
if seats[0] == '0':
    result.append(min(D, s[0]))

if seats[-1] == '0':
    result.append(min(D, N - 1 - s[-1]))

if dist:
    result.append(min(D, max(dist) // 2))

print(max(result))