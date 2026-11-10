import sys

n = int(input().rstrip())

line = [""] * 101

for _ in range(n):
    a, b = input().split()
    a = int(a)
    line[a] = b

answer = 0
for i in range(101):
    if line[i] == 'G' or line[i] == 'H':
        g = 0
        h = 0
        for j in range(i, 101):
            if line[j] != "":
                if line[j] == 'G':
                    g += 1
                else:
                    h += 1

                if (g and not h) or (h and not g) or (g == h):
                    answer = max(answer, j - i)

print(answer)