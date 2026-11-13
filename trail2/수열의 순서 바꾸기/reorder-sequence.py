N = int(input())
A = list(map(int, input().split()))

i = N - 1
while i > 0 and A[i - 1] < A[i]:
    i -= 1

print(i)