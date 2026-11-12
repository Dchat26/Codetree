n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = 0
carry = 0
for a, b in zip(A, B):
    carry += a - b
    answer += carry

print(answer)